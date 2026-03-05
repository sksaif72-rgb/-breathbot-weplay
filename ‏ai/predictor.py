from bot.database import pool

right_moves = [
"زوجين",
"متتالية",
"ثلاثة",
"فل هاوس",
"اربعة"
]

left_moves = [
"زوج",
"متتالية نفس النوع",
"AA",
"زوج و متتالية",
"لاشيء"
]


async def predict_move(card, type_):

    async with pool.acquire() as conn:

        rows = await conn.fetch(
            """
            SELECT right_result, COUNT(*) as c
            FROM training_data
            WHERE card=$1 AND type=$2
            GROUP BY right_result
            ORDER BY c DESC
            """,
            card,
            type_
        )

        if not rows:
            return {
                "result": "لا توجد بيانات",
                "prob": 0
            }

        best = rows[0]

        total = sum(r["c"] for r in rows)

        probability = round((best["c"]/total)*100,2)

        return {
            "result": best["right_result"],
            "prob": probability
        }
