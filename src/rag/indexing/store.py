"""
PostgreSQL + pgvector storage layer.

Provides batch insert, HNSW-indexed cosine similarity search,
and metadata-filtered queries.
"""

import json
import logging
import uuid
from typing import Any, Dict, List, Optional

import psycopg2
import psycopg2.extras
from psycopg2.extras import execute_values

from src.rag.common.models import EmbeddedChunk, SearchResult
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
                    embedding   VECTOR({embedding_dim}),
                    party_name  TEXT,
                    ideology    TEXT,
                    year        INTEGER,
                    topics      TEXT[],
                    confidence  INTEGER,
                    header_hierarchy JSONB,
                    chunk_type  TEXT,
                    created_at  TIMESTAMPTZ DEFAULT now()
                );
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
                (id, content, summary, embedding, party_name, ideology,
                 year, topics, confidence, header_hierarchy, chunk_type)
            VALUES %s
        """
        template = "(%s, %s, %s, %s::vector, %s, %s, %s, %s, %s, %s::jsonb, %s)"

        try:
            execute_values(cur, sql, rows, template=template, page_size=100)
            conn.commit()
            logger.info("Inserted %d chunks into '%s'.", len(rows), self.table)
            return len(rows)
        except Exception as exc:
            conn.rollback()
            logger.error("Batch insert failed: %s", exc)
            raise

    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------

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

        where_clauses: List[str] = []
        params: List[Any] = [query_embedding, query_embedding]

        if party_name:
            where_clauses.append("party_name = %s")
            params.append(party_name)
        if ideology:
            where_clauses.append("ideology = %s")
            params.append(ideology)
        if topics:
            where_clauses.append("topics && %s")
            params.append(topics)
        if year:
            where_clauses.append("year = %s")
            params.append(year)

        where_sql = ("WHERE " + " AND ".join(where_clauses)) if where_clauses else ""
        params.append(top_k)

        sql = f"""
            SELECT id, content, summary, party_name, ideology, year,
                   topics, header_hierarchy, chunk_type,
                   1 - (embedding <=> %s::vector) AS similarity
            FROM {self.table}
            {where_sql}
            ORDER BY embedding <=> %s::vector
            LIMIT %s;
        """

        try:
            cur.execute(sql, params)
            rows = cur.fetchall()
        except Exception as exc:
            logger.error("Similarity search failed: %s", exc)
            return []

        results: List[SearchResult] = []
        for row in rows:
            hh = row["header_hierarchy"] or {}
            if isinstance(hh, str):
                hh = json.loads(hh)
            results.append(
                SearchResult(
                    id=str(row["id"]),
                    content=row["content"],
                    summary=row.get("summary"),
                    party_name=row["party_name"] or "Unknown",
                    ideology=row["ideology"] or "unknown",
                    year=row["year"] or 2024,
                    topics=row["topics"] or [],
                    header_hierarchy=hh,
                    similarity=float(row["similarity"]),
                )
            )
        return results

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
