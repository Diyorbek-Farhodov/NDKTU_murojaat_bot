import os
from dotenv import load_dotenv

load_dotenv()

CHAT_ID = int(os.getenv("CHAT_ID"))
BOT_TOKEN = os.getenv("BOT_TOKEN")