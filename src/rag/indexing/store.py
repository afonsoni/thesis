"""
PostgreSQL + pgvector storage layer.

Provides batch insert, HNSW-indexed cosine similarity search, Portuguese
full-text search for hybrid retrieval, and metadata-filtered queries.
"""

import json
import logging
import uuid
from typing import Any, Dict, List, Optional, Tuple

import psycopg2
import psycopg2.extras
from psycopg2.extras import execute_values

from src.rag.common.models import EmbeddedChunk, ScoreType, SearchResult
from src.rag.indexing.bm25 import Bm25Index, parse_tsvector, restore_suffix_accents
from src.utils.config_loader import config

logger = logging.getLogger(__name__)


class VectorStore:
    """PostgreSQL + pgvector interface for storing and searching embeddings."""

    def __init__(self, db_config: Optional[Dict[str, Any]] = None):
        if db_config is None:
            db_config = {
                "host": config.get("postgresql.host", "localhost"),
                "port": int(config.get("postgresql.port", 5432)),
                "database": config.get("postgresql.database", "ragdb"),
                "user": config.get("postgresql.user", "postgres"),
                "password": config.get("postgresql.password", "postgres"),
            }
        self.db_config = db_config
        self.table = config.get("postgresql.table_name", "party_programs")
        self.connection: Optional[psycopg2.extensions.connection] = None
        self._bm25: Optional[Bm25Index] = None  # built on first lexical search

    # ------------------------------------------------------------------
    # Connection management
    # ------------------------------------------------------------------

    def connect(self) -> bool:
        """Open a connection to PostgreSQL."""
        try:
            self.connection = psycopg2.connect(**self.db_config)
            self.connection.autocommit = False
            logger.info("Connected to PostgreSQL at %s:%s", self.db_config["host"], self.db_config["port"])
            return True
        except Exception as exc:
            logger.error("Failed to connect to PostgreSQL: %s", exc)
            return False

    def close(self):
        """Close the current connection."""
        if self.connection and not self.connection.closed:
            self.connection.close()
            logger.info("Connection closed.")

    def _ensure_connected(self):
        if self.connection is None or self.connection.closed:
            if not self.connect():
                raise ConnectionError("Cannot connect to PostgreSQL")

    def _conn(self) -> psycopg2.extensions.connection:
        """Return an active connection with concrete type for static checkers."""
        self._ensure_connected()
        conn = self.connection
        if conn is None or conn.closed:
            raise ConnectionError("Cannot connect to PostgreSQL")
        return conn

    # ------------------------------------------------------------------
    # Schema
    # ------------------------------------------------------------------

    def create_table(self, embedding_dim: int = 1536):
        """
        Create the pgvector extension, the main table, and an HNSW index.
        """
        conn = self._conn()
        cur = conn.cursor()
        try:
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")

            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.table} (
                    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    content     TEXT NOT NULL,
                    summary     TEXT,
                    parent_content TEXT,
                    embedding   VECTOR({embedding_dim}),
                    party_name  TEXT,
                    ideology    TEXT,
                    year        INTEGER,
                    topics      TEXT[],
                    confidence  INTEGER,
                    header_hierarchy JSONB,
                    chunk_type  TEXT,
                    created_at  TIMESTAMPTZ DEFAULT now(),
                    -- Lexical half of hybrid search. Generated, so it can never
                    -- drift out of sync with content on insert or update.
                    content_tsv TSVECTOR GENERATED ALWAYS AS (
                        to_tsvector('portuguese', coalesce(content, ''))
                    ) STORED
                );
            """)

            # Bring pre-existing tables up to the current schema — CREATE TABLE
            # IF NOT EXISTS is a no-op on them, so new columns must be added.
            cur.execute(f"""
                ALTER TABLE {self.table}
                ADD COLUMN IF NOT EXISTS parent_content TEXT;
            """)
            cur.execute(f"""
                ALTER TABLE {self.table}
                ADD COLUMN IF NOT EXISTS content_tsv TSVECTOR GENERATED ALWAYS AS (
                    to_tsvector('portuguese', coalesce(content, ''))
                ) STORED;
            """)

            # HNSW index for fast approximate nearest-neighbour search
            cur.execute(f"""
                CREATE INDEX IF NOT EXISTS idx_{self.table}_embedding_hnsw
                ON {self.table}
                USING hnsw (embedding vector_cosine_ops)
                WITH (m = 16, ef_construction = 64);
            """)

            # B-tree indexes for common filter columns
            for col in ("party_name", "ideology", "year"):
                cur.execute(f"""
                    CREATE INDEX IF NOT EXISTS idx_{self.table}_{col}
                    ON {self.table} ({col});
                """)

            # GIN index for topics array
            cur.execute(f"""
                CREATE INDEX IF NOT EXISTS idx_{self.table}_topics
                ON {self.table} USING gin (topics);
            """)

            # GIN index backing the full-text (lexical) half of hybrid search
            cur.execute(f"""
                CREATE INDEX IF NOT EXISTS idx_{self.table}_content_tsv
                ON {self.table} USING gin (content_tsv);
            """)

            conn.commit()
            logger.info("Table '%s' and indexes created / verified.", self.table)
        except Exception as exc:
            conn.rollback()
            logger.error("Error creating table: %s", exc)
            raise

    def drop_table(self):
        """Drop the main table (use with care!)."""
        conn = self._conn()
        cur = conn.cursor()
        try:
            cur.execute(f"DROP TABLE IF EXISTS {self.table} CASCADE;")
            conn.commit()
            self._bm25 = None
            logger.warning("Table '%s' dropped.", self.table)
        except Exception as exc:
            conn.rollback()
            logger.error("Error dropping table: %s", exc)
            raise

    # ------------------------------------------------------------------
    # Insert
    # ------------------------------------------------------------------

    def insert_chunks(self, chunks: List[EmbeddedChunk]) -> int:
        """
        Batch-insert embedded chunks.  Returns the number of rows inserted.
        """
        if not chunks:
            return 0

        conn = self._conn()
        cur = conn.cursor()

        rows = []
        for c in chunks:
            rows.append((
                str(uuid.uuid4()),
                c.content,
                c.summary,
                c.parent_content,
                c.embedding,
                c.party_name,
                c.ideology,
                c.year,
                c.topics,
                c.topic_classification.confianca if c.topic_classification else None,
                json.dumps(c.metadata),
                c.chunk_type,
            ))

        sql = f"""
            INSERT INTO {self.table}
                (id, content, summary, parent_content, embedding, party_name,
                 ideology, year, topics, confidence, header_hierarchy, chunk_type)
            VALUES %s
        """
        template = "(%s, %s, %s, %s, %s::vector, %s, %s, %s, %s, %s, %s::jsonb, %s)"

        try:
            execute_values(cur, sql, rows, template=template, page_size=100)
            conn.commit()
            self._bm25 = None  # term statistics changed
            logger.info("Inserted %d chunks into '%s'.", len(rows), self.table)
            return len(rows)
        except Exception as exc:
            conn.rollback()
            logger.error("Batch insert failed: %s", exc)
            raise

    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------

    # Columns every search path hydrates a SearchResult from.
    _RESULT_COLUMNS = (
        "id, content, summary, parent_content, party_name, ideology, year, "
        "topics, header_hierarchy, chunk_type"
    )

    @staticmethod
    def _build_filters(
        party_name: Optional[str] = None,
        ideology: Optional[str] = None,
        topics: Optional[List[str]] = None,
        year: Optional[int] = None,
    ) -> Tuple[List[str], List[Any]]:
        """Build the shared metadata WHERE clauses and their bound parameters."""
        clauses: List[str] = []
        params: List[Any] = []
        if party_name:
            clauses.append("party_name = %s")
            params.append(party_name)
        if ideology:
            clauses.append("ideology = %s")
            params.append(ideology)
        if topics:
            clauses.append("topics && %s")
            params.append(topics)
        if year:
            clauses.append("year = %s")
            params.append(year)
        return clauses, params

    @staticmethod
    def _row_to_result(
        row: Dict[str, Any],
        score: float,
        score_type: ScoreType,
    ) -> SearchResult:
        """Hydrate one result row, decoding the JSONB header metadata."""
        hh = row["header_hierarchy"] or {}
        if isinstance(hh, str):
            hh = json.loads(hh)
        return SearchResult(
            id=str(row["id"]),
            content=row["content"],
            summary=row.get("summary"),
            parent_content=row.get("parent_content"),
            party_name=row["party_name"] or "Unknown",
            ideology=row["ideology"] or "unknown",
            year=row["year"] or 2024,
            topics=row["topics"] or [],
            header_hierarchy=hh,
            similarity=score,
            score_type=score_type,
        )

    def _bm25_index(self, cur) -> Bm25Index:
        """Term statistics of the whole table, loaded once per store instance."""
        if self._bm25 is None:
            cur.execute(f"SELECT id::text AS id, content_tsv::text AS tsv FROM {self.table}")
            self._bm25 = Bm25Index((r["id"], parse_tsvector(r["tsv"])) for r in cur.fetchall())
            logger.info("BM25 index: %d chunks, %d lexemes", self._bm25.n, len(self._bm25.postings))
        return self._bm25

    def lexical_search(
        self,
        query: str,
        top_k: int = 5,
        party_name: Optional[str] = None,
        ideology: Optional[str] = None,
        topics: Optional[List[str]] = None,
        year: Optional[int] = None,
    ) -> List[SearchResult]:
        """
        Portuguese BM25 search — the lexical half of hybrid retrieval.

        Complements dense search on the cases embeddings handle worst: rare exact
        tokens such as acronyms and programme names (``USF``, ``TMRG``, ``RES_U``,
        ``Cheque-Dentista``), which carry little distributional signal but are
        precisely what a user quotes when asking about them.

        The query goes through the same Portuguese ``to_tsvector`` as the stored
        ``content_tsv`` (stemming, stop words), and chunks are ranked by BM25 over
        those lexemes (:mod:`bm25`): any query term can match, and rare terms
        weigh more. Metadata filters are applied in SQL. Scores are on their own
        scale — see :class:`ScoreType.LEXICAL` — and are only comparable to dense
        scores after rank-based fusion.

        Returns an empty list when the query has no searchable Portuguese terms
        (e.g. only stop-words), which is a normal outcome, not an error.
        """
        conn = self._conn()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        try:
            index = self._bm25_index(cur)
            cur.execute("SELECT to_tsvector('portuguese', %s)::text AS q", (restore_suffix_accents(query),))
            terms = list(parse_tsvector(cur.fetchone()["q"]))
            if not terms:
                return []

            allowed = None
            clauses, params = self._build_filters(party_name, ideology, topics, year)
            if clauses:
                cur.execute(f"SELECT id::text AS id FROM {self.table} WHERE " + " AND ".join(clauses), params)
                allowed = {r["id"] for r in cur.fetchall()}

            ranked = index.top_k(terms, top_k, allowed)
            if not ranked:
                return []
            cur.execute(
                f"SELECT {self._RESULT_COLUMNS} FROM {self.table} WHERE id::text = ANY(%s)",
                ([doc_id for doc_id, _ in ranked],),
            )
            rows = {str(r["id"]): r for r in cur.fetchall()}
        except Exception:
            # Roll back so the connection stays usable, then let the error
            # through: returning [] made a broken index read as zero recall.
            conn.rollback()
            raise

        return [
            self._row_to_result(rows[doc_id], score, ScoreType.LEXICAL)
            for doc_id, score in ranked
            if doc_id in rows
        ]

    def similarity_search(
        self,
        query_embedding: List[float],
        top_k: int = 5,
        party_name: Optional[str] = None,
        ideology: Optional[str] = None,
        topics: Optional[List[str]] = None,
        year: Optional[int] = None,
    ) -> List[SearchResult]:
        """
        Cosine-similarity search with optional metadata filters.

        Args:
            query_embedding: Query vector (same dimension as stored embeddings).
            top_k: Number of results to return.
            party_name: Filter by exact party name.
            ideology: Filter by ``left`` / ``right``.
            topics: Filter by any overlap with the chunk's topics array.
            year: Filter by election year.

        Returns:
            List of ``SearchResult`` ordered by descending similarity.
        """
        conn = self._conn()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        where_clauses, filter_params = self._build_filters(
            party_name, ideology, topics, year
        )
        where_sql = ("WHERE " + " AND ".join(where_clauses)) if where_clauses else ""
        params: List[Any] = [query_embedding, *filter_params, query_embedding, top_k]

        sql = f"""
            SELECT {self._RESULT_COLUMNS},
                   1 - (embedding <=> %s::vector) AS similarity
            FROM {self.table}
            {where_sql}
            ORDER BY embedding <=> %s::vector
            LIMIT %s;
        """

        try:
            cur.execute(sql, params)
            rows = cur.fetchall()
        except Exception:
            conn.rollback()
            raise

        return [
            self._row_to_result(row, float(row["similarity"]), ScoreType.COSINE)
            for row in rows
        ]

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------

    def count(self, party_name: Optional[str] = None) -> int:
        """Count rows, optionally filtered by party."""
        conn = self._conn()
        cur = conn.cursor()
        if party_name:
            cur.execute(f"SELECT count(*) FROM {self.table} WHERE party_name = %s;", (party_name,))
        else:
            cur.execute(f"SELECT count(*) FROM {self.table};")
        row = cur.fetchone()
        return int(row[0]) if row else 0

    def get_distinct_parties(self) -> List[str]:
        """Return list of distinct party names in the store."""
        conn = self._conn()
        cur = conn.cursor()
        cur.execute(f"SELECT DISTINCT party_name FROM {self.table} WHERE party_name IS NOT NULL ORDER BY party_name;")
        return [row[0] for row in cur.fetchall()]

    def test_connection(self) -> bool:
        """Quick connectivity & pgvector check."""
        try:
            conn = self._conn()
            cur = conn.cursor()
            cur.execute("SELECT version();")
            row = cur.fetchone()
            ver = row[0] if row else "unknown"
            logger.info("PostgreSQL version: %s", ver)
            cur.execute("SELECT * FROM pg_extension WHERE extname = 'vector';")
            if cur.fetchone():
                logger.info("pgvector extension is installed.")
            else:
                logger.warning("pgvector extension NOT found.")
            return True
        except Exception as exc:
            logger.error("Connection test failed: %s", exc)
            return False
