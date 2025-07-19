from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get('TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

app = Flask(__name__)

bot_app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Bot avviato!")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Bot attivo e funzionante.")

bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(CommandHandler("status", status))

@app.route('/')
def home():
    return 'Bot is running!'

@app.route(f"/{TOKEN}", methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    bot_app.update_queue.put(update)
    return 'ok'

if __name__ == '__main__':
    bot_app.run_polling()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
