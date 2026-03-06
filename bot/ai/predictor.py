from bot.database import pool

async def predict(card, suit):

    query = """
    SELECT hand_type, COUNT(*) as c
    FROM training_data
    WHERE card=$1 AND suit=$2
    GROUP BY hand_type
    ORDER BY c DESC
    LIMIT 1
    """

    async with pool.acquire() as conn:
        row = await conn.fetchrow(query, card, suit)

    if row:
        return row["hand_type"]

    return "لا يوجد بيانات كافية"
