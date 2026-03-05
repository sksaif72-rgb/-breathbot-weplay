from bot.database import pool
from ai.montecarlo import monte_carlo_simulation


async def predict_move(card, type_):

    async with pool.acquire() as conn:

        rows = await conn.fetch(
            """
            SELECT right_result, COUNT(*) as c
            FROM training_data
            WHERE card=$1 AND type=$2
            GROUP BY right_result
            """,
            card,
            type_
        )

        if not rows:

            mc_result, mc_prob = monte_carlo_simulation()

            return {
                "result": mc_result,
                "prob": mc_prob
            }

        stats = {}

        total = 0

        for r in rows:

            stats[r["right_result"]] = r["c"]
            total += r["c"]

        best = max(stats, key=stats.get)

        prob = round((stats[best] / total) * 100, 2)

        mc_result, mc_prob = monte_carlo_simulation()

        final_prob = round((prob + mc_prob) / 2, 2)

        return {
            "result": best,
            "prob": final_prob
        }
