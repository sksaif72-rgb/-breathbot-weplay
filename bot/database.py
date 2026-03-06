import os
import psycopg2


DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():

    conn = psycopg2.connect(
        DATABASE_URL,
        sslmode="require"
    )

    return conn
