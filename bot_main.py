# bot_main.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = ""

WEB_APP_URL = ""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎮 Играть в Пинг-Понг", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Нажми кнопку, чтобы играть в Пинг-Понг!", reply_markup=reply_markup)

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен.")
    app.run_polling()

if __name__ == "__main__":
    from multiprocessing import Process
    from local_webapp import run_flask_app

    flask_process = Process(target=run_flask_app)
    flask_process.start()

    try:
        run_bot()
    finally:
        flask_process.terminate()
