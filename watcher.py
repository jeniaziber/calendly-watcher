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
print(json.dumps(data, indent=2))

# Зберігаємо відповідь для дебагу
with open("debug.json", "w") as f:
    json.dump(data, f, indent=2)

available_slot = None

for day in data.get("days", []):
    if day.get("date") == TARGET_DATE:
        for slot in day.get("spots", []):
            if slot.get("time") in TARGET_TIMES:
                available_slot = slot.get("time")


print(f"Slot {TARGET_DATE}: {available_slot}")
send("✅ Calendly watcher працює")


state = load_state()

previous_slot = state.get("last_slot")


if available_slot and available_slot != previous_slot:
    send(
        f"""🎾 З'явився вільний слот!

📅 Дата: {TARGET_DATE}
⏰ Час: {available_slot}

Бронюй зараз:

https://calendly.com/subscriptions-bo2bo/tennis?month=2026-07
"""
    )

save_state({
    "last_slot": available_slot
})
