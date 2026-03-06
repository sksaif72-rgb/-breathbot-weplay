import sqlite3
import os
from datetime import datetime

DB_FILE = os.path.join(os.path.dirname(__file__), "breathbot.db")


def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # المشتركين
    cur.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        joined_at TEXT
    )
    """)

    # المدربين
    cur.execute("""
    CREATE TABLE IF NOT EXISTS trainers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        name TEXT,
        created_at TEXT
    )
    """)

    # الجولات
    cur.execute("""
    CREATE TABLE IF NOT EXISTS rounds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        trainer_id INTEGER,
        card_rank TEXT,
        card_suit TEXT,
        result TEXT,
        created_at TEXT
    )
    """)

    # الاحصائيات
    cur.execute("""
    CREATE TABLE IF NOT EXISTS stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        card_rank TEXT,
        card_suit TEXT,
        total INTEGER DEFAULT 0
    )
    """)

    # افضل دقيقة
    cur.execute("""
    CREATE TABLE IF NOT EXISTS best_minutes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        minute TEXT,
        card_type TEXT,
        card_rank TEXT,
        score INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# المشتركين
# -----------------------------

def add_subscriber(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO subscribers (telegram_id, joined_at)
    VALUES (?, ?)
    """, (user_id, datetime.utcnow().isoformat()))

    conn.commit()
    conn.close()


def get_all_subscribers():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT telegram_id FROM subscribers")
    rows = cur.fetchall()

    conn.close()
    return [r["telegram_id"] for r in rows]


# -----------------------------
# المدربين
# -----------------------------

def add_trainer(user_id, name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO trainers (telegram_id, name, created_at)
    VALUES (?, ?, ?)
    """, (user_id, name, datetime.utcnow().isoformat()))

    conn.commit()
    conn.close()


def is_trainer(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM trainers WHERE telegram_id=?", (user_id,))
    row = cur.fetchone()

    conn.close()
    return row is not None


# -----------------------------
# الجولات
# -----------------------------

def add_round(trainer_id, rank, suit, result):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO rounds (trainer_id, card_rank, card_suit, result, created_at)
    VALUES (?, ?, ?, ?, ?)
    """, (trainer_id, rank, suit, result, datetime.utcnow().isoformat()))

    conn.commit()
    conn.close()


# -----------------------------
# الاحصائيات
# -----------------------------

def update_stats(rank, suit):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT id,total FROM stats
    WHERE card_rank=? AND card_suit=?
    """, (rank, suit))

    row = cur.fetchone()

    if row:
        cur.execute("""
        UPDATE stats
        SET total = total + 1
        WHERE id=?
        """, (row["id"],))
    else:
        cur.execute("""
        INSERT INTO stats (card_rank, card_suit, total)
        VALUES (?, ?, 1)
        """, (rank, suit))

    conn.commit()
    conn.close()


def get_stats_by_rank(rank):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT card_suit,total
    FROM stats
    WHERE card_rank=?
    """, (rank,))

    rows = cur.fetchall()
    conn.close()

    return rows


# -----------------------------
# افضل دقيقة
# -----------------------------

def update_best_minute(minute, suit, rank):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT id,score
    FROM best_minutes
    WHERE minute=? AND card_type=? AND card_rank=?
    """, (minute, suit, rank))

    row = cur.fetchone()

    if row:
        cur.execute("""
        UPDATE best_minutes
        SET score = score + 1
        WHERE id=?
        """, (row["id"],))
    else:
        cur.execute("""
        INSERT INTO best_minutes (minute, card_type, card_rank, score)
        VALUES (?, ?, ?, 1)
        """, (minute, suit, rank))

    conn.commit()
    conn.close()


def get_best_minutes():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT minute,card_type,card_rank,score
    FROM best_minutes
    ORDER BY score DESC
    LIMIT 5
    """)

    rows = cur.fetchall()
    conn.close()

    return rows
