import json
import os
import requests

from notifier import send
from config import *

STATE_FILE = "state.json"


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"available": False}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


params = {
    "timezone": TIMEZONE,
    "diagnostics": "false",
    "range_start": TARGET_DATE,
    "range_end": TARGET_DATE,
    "scheduling_link_uuid": SCHEDULING_UUID,
}

response = requests.get(
    URL,
    params=params,
    timeout=30,
)

response.raise_for_status()

data = response.json()

# Зберігаємо відповідь для дебагу
with open("debug.json", "w") as f:
    json.dump(data, f, indent=2)

available_slot = False

for day in data.get("days", []):
    for slot in day.get("spots", []):
        if slot.get("time") == TARGET_TIME:
            available_slot = True


if available_slot:
    send(
        f"""🎾 З'явився вільний слот!

📅 Дата: {TARGET_DATE}
⏰ Час: {TARGET_TIME}

Бронюй зараз:

https://calendly.com/subscriptions-bo2bo/tennis?month=2026-07
"""
    )
