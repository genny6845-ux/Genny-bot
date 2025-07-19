from flask import Flask, request
import telegram
import os

TOKEN = os.environ.get('TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running!'

@app.route('/{}'.format(TOKEN), methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text == "/start":
        bot.send_message(chat_id=chat_id, text="Bot avviato!")
    elif text == "/status":
        bot.send_message(chat_id=chat_id, text="Bot attivo e funzionante.")
    else:
        bot.send_message(chat_id=chat_id, text="Comando non riconosciuto.")

    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
