import logging

from telegram.ext import ApplicationBuilder

from bot.config import BOT_TOKEN
from bot.handlers import start, guess, training, stats, admin


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def main():
    print("Starting bot...")

    # إنشاء التطبيق
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # تسجيل الهاندلرز
    application.add_handler(start.start_handler)
    application.add_handler(guess.guess_handler)
    application.add_handler(training.training_handler)
    application.add_handler(stats.stats_handler)
    application.add_handler(admin.admin_handler)

    print("Bot is running...")
    
    # تشغيل البوت
    application.run_polling()


if __name__ == "__main__":
    main()
