import os
import psycopg2


DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():

    conn = psycopg2.connect(
        DATABASE_URL,
        sslmode="require"
    )

    return conn
def get_card_stats(card):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT type, right_attack, COUNT(*) as count
        FROM training_data
        WHERE card = %s
        GROUP BY type, right_attack
        ORDER BY count DESC
    """, (card,))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    result = []

    for row in rows:
        result.append({
            "type": row[0],
            "right_attack": row[1],
            "count": row[2]
        })

    return result
