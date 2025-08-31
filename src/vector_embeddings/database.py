"""
This file contains database operations for storing and searching embeddings.

The database chosen for this implementation is PostgreSQL, using pgvector for vector embeddings.

The schema is designed to store the embeddings along with their metadata, allowing for efficient searching and retrieval.
"""

import psycopg2
from psycopg2.extras import execute_values
from sentence_transformers import SentenceTransformer
import openai
from typing import List, Dict, Optional


class DB:
    """Handles all vector database operations for political content embeddings"""

    def __init__(
        self,
        model_name="PORTULAN/serafim-900m-portuguese-pt-sentence-encoder-ir",
        db_config=None,
    ):
        self.model = SentenceTransformer(model_name)
        self.embedding_dim = 1536  # serafim 900m dimension
        self.table_name = "party_programs"  # Updated to match your schema

        # Docker/OrbStack PostgreSQL configuration
        if db_config is None:
            db_config = {
                "host": "localhost",
                "port": 5432,
                "database": "ragdb",
                "user": "postgres",
                "password": "postgres",  # To be updated
            }

        self.db_config = db_config
        self.connection = None

    def connect(self):
        """Establish connection to PostgreSQL database running in Docker"""
        try:
            print(
                f"Connecting to PostgreSQL at {self.db_config['host']}:{self.db_config['port']}"
            )
            self.connection = psycopg2.connect(**self.db_config)
            print("Successfully connected to PostgreSQL database")
            return True
        except psycopg2.OperationalError as e:
            print(f"Error connecting to database: {e}")
            print("Make sure your PostgreSQL Docker container is running:")
            print("docker ps | grep postgres")
            return False
        except Exception as e:
            print(f"Unexpected error connecting to database: {e}")
            return False

    def close_connection(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            print("Database connection closed")

    def test_connection(self):
        """Test the database connection"""
        if self.connect():
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute("SELECT version();")
                    version = cursor.fetchone()
                    print(f"PostgreSQL version: {version[0]}")

                    # Check if pgvector extension is available
                    cursor.execute(
                        "SELECT * FROM pg_extension WHERE extname = 'vector';"
                    )
                    vector_ext = cursor.fetchone()
                    if vector_ext:
                        print("pgvector extension is installed")
                    else:
                        print("Warning: pgvector extension not found")

                return True
            except Exception as e:
                print(f"Error testing connection: {e}")
                return False
            finally:
                self.close_connection()
        return False

    def create_table(self):
        """Create the PostgreSQL table if it doesn't exist"""
        if not self.connection:
            if not self.connect():
                return False

        try:
            with self.connection.cursor() as cursor:
                # First, ensure the vector extension is created
                cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")

                # Create the table matching your existing schema
                cursor.execute(
                    f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    content TEXT NOT NULL,
                    embedding VECTOR({self.embedding_dim}),
                    party_name TEXT,
                    ideology TEXT,
                    year INTEGER,
                    topic TEXT
                );
                """
                )

                self.connection.commit()
                print(f"Table {self.table_name} created successfully")
                return True

        except Exception as e:
            print(f"Error creating table: {e}")
            if self.connection:
                self.connection.rollback()
            return False

    def insert_data(
        self, content, embedding, party_name=None, ideology=None, year=None, topic=None
    ):
        """Insert data into the PostgreSQL table"""
        if not self.connection:
            if not self.connect():
                return False

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f"""
                INSERT INTO {self.table_name} (content, embedding, party_name, ideology, year, topic)
                VALUES (%s, %s, %s, %s, %s, %s);
                """,
                    (content, embedding, party_name, ideology, year, topic),
                )
                self.connection.commit()
                print("Data inserted successfully")
                return True

        except Exception as e:
            print(f"Error inserting data: {e}")
            if self.connection:
                self.connection.rollback()
            return False

    def get_data(self):
        """Retrieve data from the PostgreSQL table"""
        if not self.connection:
            if not self.connect():
                return False

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {self.table_name};")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                return True

        except Exception as e:
            print(f"Error retrieving data: {e}")
            return False

    def get_data_from_embeddings(self, embedding):
        """Retrieve data from the PostgreSQL table based on the embedding"""
        if not self.connection:
            if not self.connect():
                return False

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT * FROM {self.table_name} WHERE embedding = %s;",
                    (embedding,),
                )
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                return True

        except Exception as e:
            print(f"Error retrieving data: {e}")
            return False
