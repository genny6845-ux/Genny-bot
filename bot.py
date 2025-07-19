import os
import requests
import time

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    requests.post(url, data=payload)

def check_portfolio():
    # Qui metteremo la logica per leggere i dati da eToro
    # Per ora simuliamo un ribilanciamento
    return "🔔 Ribilanciamento completato: +3% rendimento 🚀"

if __name__ == "__main__":
    while True:
        message = check_portfolio()
        send_message(message)
        time.sleep(3600)  # ogni ora
