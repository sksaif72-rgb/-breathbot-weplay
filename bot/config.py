import os

# توكن البوت
BOT_TOKEN = os.getenv("BOT_TOKEN")

# كود وضع التدريب
TRAINING_CODE = os.getenv("TRAINING_CODE", "12345")

# رابط قاعدة البيانات Neon
DATABASE_URL = os.getenv("DATABASE_URL")
