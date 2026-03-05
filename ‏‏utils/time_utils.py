from bot.database import pool


async def best_minute(result):

    async with pool.acquire() as conn:

        row = await conn.fetchrow(
            """
            SELECT minute, COUNT(*) as c
            FROM training_data
            WHERE right_result=$1
            GROUP BY minute
            ORDER BY c DESC
            LIMIT 1
            """,
            result
        )

    if not row:
        return None

    return row["minute"]
