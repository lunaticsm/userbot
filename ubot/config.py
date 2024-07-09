import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    1983980399,
]

KYNAN = list(map(int, os.getenv("KYNAN", "1983980399").split()))

API_ID = int(os.getenv("API_ID", ""))

API_HASH = os.getenv("API_HASH", "")

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

OWNER_ID = int(os.getenv("OWNER_ID", ""))

USER_ID = list(map(int, os.getenv("USER_ID", "").split()))

LOG_UBOT = int(os.getenv("LOG_UBOT", ""))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

RMBG_API = os.getenv("RMBG_API", "")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "",
)
