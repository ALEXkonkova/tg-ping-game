# bot_main.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7031125260:AAEHrZnuqnppKQSXPYdmDaAmnMRQFVBSWGE"  # вставь сюда свой токен

WEB_APP_URL = "http://6034a861-dd49-43f0-9cf4-8be4735aba34"

#WEB_APP_URL = "https://05b4-2a0c-16c0-515-6d-00-68b3.ngrok-free.app"  # локальный адрес игры

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
