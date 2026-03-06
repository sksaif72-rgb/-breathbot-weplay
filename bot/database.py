import asyncpg
from .config import DATABASE_URL

pool = None

async def connect():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)

async def add_user(user_id):

    query = """
    INSERT INTO users(user_id)
    VALUES($1)
    ON CONFLICT DO NOTHING
    """

    async with pool.acquire() as conn:
        await conn.execute(query, user_id)


async def add_training(card, suit, hand_type, minute):

    query = """
    INSERT INTO training_data(card,suit,hand_type,minute)
    VALUES($1,$2,$3,$4)
    """

    async with pool.acquire() as conn:
        await conn.execute(query, card, suit, hand_type, minute)


async def get_best_minute(hand_type):

    query = """
    SELECT minute, COUNT(*) as c
    FROM training_data
    WHERE hand_type=$1
    GROUP BY minute
    ORDER BY c DESC
    LIMIT 1
    """

    async with pool.acquire() as conn:
        row = await conn.fetchrow(query, hand_type)

    return row


async def get_stats(card):

    query = """
    SELECT suit, hand_type, COUNT(*) as c
    FROM training_data
    WHERE card=$1
    GROUP BY suit,hand_type
    ORDER BY c DESC
    """

    async with pool.acquire() as conn:
        rows = await conn.fetch(query, card)

    return rows
