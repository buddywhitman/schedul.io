# messaging_platforms/telegram_api.py

import requests

def get_telegram_messages(bot_token):
    api_url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
    response = requests.get(api_url)
    messages = response.json().get('result', [])
    return messages
