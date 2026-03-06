import os
import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)


# ==============================
# USERS
# ==============================

def add_user(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO users (user_id)
        VALUES (%s)
        ON CONFLICT (user_id) DO NOTHING
        """,
        (user_id,)
    )

    conn.commit()
    cur.close()
    conn.close()


# ==============================
# TRAINING DATA
# ==============================

def add_training(card, suit, minute, result_type):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO training_data (card, suit, minute, result_type)
        VALUES (%s, %s, %s, %s)
        """,
        (card, suit, minute, result_type)
    )

    conn.commit()
    cur.close()
    conn.close()


# ==============================
# STATS
# ==============================

def get_stats(card, suit):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT result_type, COUNT(*) as total
        FROM training_data
        WHERE card=%s AND suit=%s
        GROUP BY result_type
        ORDER BY total DESC
        """,
        (card, suit)
    )

    data = cur.fetchall()

    cur.close()
    conn.close()

    return data
