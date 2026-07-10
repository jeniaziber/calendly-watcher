import requests
from config import BOT_TOKEN, CHAT_ID


def send(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        response.raise_for_status()
        url,
        json={
            "chat_id": CHAT_ID,
            "text": message,
        },
        timeout=30,
    )

    response.raise_for_status()
