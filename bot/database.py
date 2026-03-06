import asyncpg
import os

pool = None


async def connect_db():
    global pool

    pool = await asyncpg.create_pool(
        os.getenv("DATABASE_URL")
    )


async def add_user(user_id):

    async with pool.acquire() as conn:

        await conn.execute(
            """
            INSERT INTO users (user_id)
            VALUES ($1)
            ON CONFLICT (user_id) DO NOTHING
            """,
            user_id
        )


async def get_user(user_id):

    async with pool.acquire() as conn:

        return await conn.fetchrow(
            "SELECT * FROM users WHERE user_id=$1",
            user_id
        )
async def create_tables():

    async with pool.acquire() as conn:

        await conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                user_id BIGINT UNIQUE
            );
            """
        )
