from telegram.ext import Updater

from bot.config import BOT_TOKEN

# handlers
from bot.handlers.start import register_start_handlers
from bot.handlers.subscription import register_subscription_handlers
from bot.handlers.training import register_training_handlers
from bot.handlers.stats import register_stats_handlers
from bot.handlers.predict import register_predict_handlers


def main():

    updater = Updater(BOT_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    # تسجيل الهاندلرز
    register_start_handlers(dispatcher)
    register_subscription_handlers(dispatcher)
    register_training_handlers(dispatcher)
    register_stats_handlers(dispatcher)
    register_predict_handlers(dispatcher)

    print("BREATHBOT-Weplay started...")

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
