import asyncpg
from bot.config import DATABASE_URL

pool = None


async def connect_db():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)


async def create_tables():

    async with pool.acquire() as conn:

        await conn.execute("""

        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            telegram_id BIGINT UNIQUE,
            username TEXT,
            created_at TIMESTAMP DEFAULT NOW()
        );

        """)

        await conn.execute("""

        CREATE TABLE IF NOT EXISTS subscriptions(
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            expire_at TIMESTAMP
        );

        """)

        await conn.execute("""

        CREATE TABLE IF NOT EXISTS activation_codes(
            id SERIAL PRIMARY KEY,
            code TEXT UNIQUE,
            days INTEGER,
            used BOOLEAN DEFAULT FALSE,
            used_by BIGINT
        );

        """)

        await conn.execute("""

        CREATE TABLE IF NOT EXISTS trainers(
            id SERIAL PRIMARY KEY,
            telegram_id BIGINT UNIQUE,
            name TEXT
        );

        """)

        await conn.execute("""

        CREATE TABLE IF NOT EXISTS training_data(
            id SERIAL PRIMARY KEY,
            card TEXT,
            type TEXT,
            minute INTEGER,
            right_result TEXT,
            left_result TEXT,
            created_at TIMESTAMP DEFAULT NOW()
        );

        """)

        await conn.execute("""

        CREATE TABLE IF NOT EXISTS predictions(
            id SERIAL PRIMARY KEY,
            card TEXT,
            type TEXT,
            minute INTEGER,
            predicted TEXT,
            probability FLOAT
        );

        """)
