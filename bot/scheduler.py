from apscheduler.schedulers.asyncio import AsyncIOScheduler

from utils.time_utils import best_minute_for_result
from bot.database import pool

scheduler = AsyncIOScheduler()


async def broadcast_best_times(bot):

    four = await best_minute_for_result("اربعة")
    aa = await best_minute_for_result("AA")
    fh = await best_minute_for_result("فل هاوس")

    text = "افضل الاوقات المتوقعة:\n\n"

    if four:
        text += f"اربعة : الدقيقة {four}\n"

    if aa:
        text += f"AA : الدقيقة {aa}\n"

    if fh:
        text += f"فل هاوس : الدقيقة {fh}\n"

    async with pool.acquire() as conn:

        users = await conn.fetch(
            """
            SELECT telegram_id
            FROM users
            """
        )

    for u in users:

        try:
            await bot.send_message(u["telegram_id"], text)
        except:
            pass


def start_scheduler(bot):

    scheduler.add_job(
        broadcast_best_times,
        "interval",
        minutes=30,
        args=[bot]
    )

    scheduler.start()
