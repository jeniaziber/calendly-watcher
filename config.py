from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

EVENT_UUID = "3ae726fe-ec85-42ce-9979-2660f20827de"
SCHEDULING_UUID = "cxyq-p94-zkw"

TIMEZONE = "Europe/Berlin"

TARGET_DATE = "2026-07-12"
TARGET_TIME = "12:00"

URL = (
    f"https://calendly.com/api/booking/event_types/"
    f"{EVENT_UUID}/calendar/range"
)
