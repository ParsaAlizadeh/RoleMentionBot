import os
import re
import telegram
from dotenv import load_dotenv

load_dotenv()
PREFIX = os.getenv("PREFIX", ";")
BATCH = int(os.getenv("BATCH", 7))
MAX_ROLES = int(os.getenv("MAX_ROLES", 10))
ROLE_PATTERN = re.compile(r"(\s|^)@([a-zA-Z0-9_]{5,32})")
IGNORE_STATUS = (telegram.ChatMember.LEFT,
                 telegram.ChatMember.KICKED,
                 telegram.ChatMember.RESTRICTED)
ADMIN_STATUS = (telegram.ChatMember.ADMINISTRATOR,
                telegram.ChatMember.CREATOR)

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise Exception("TOKEN not found")

DB_FILE = os.getenv("DBFILE", "db/role.db")

REGISTERED = os.getenv("REGISTERED")
if REGISTERED is None:
    raise Exception("No registered groups")
REGISTERED = set(map(int, REGISTERED.split(':')))

DEBUG = os.getenv("DEBUG", "true")
DEBUG = DEBUG.lower() in ["true", "yes"]
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
CERT_FILEPATH = os.getenv("CERT_FILEPATH")
PORT = os.getenv("PORT")
if PORT is not None:
    PORT = int(PORT)
