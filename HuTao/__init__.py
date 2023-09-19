#MIT License
#Copyright (c) 2023, ©NovaNetworks

import time
from logging import ERROR, INFO, StreamHandler, basicConfig, getLogger, handlers
from pyrogram import Client
from async_pymongo import AsyncClient
import pytz

from HuTao.Config import (
    API_HASH,
    API_ID,
    BOT_TOKEN,
    TIMEZONE,
    LOG_CHANNEL_ID,
    SUDO,
    DB_URL,
    LOG_CHANNEL_ID,
    OWNER,
    SQL_URL,
    COMMAND_HANDLER,
    SUPPORT_CHAT,
)

#LOGGER SETUP
basicConfig(
    level=INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s.%(funcName)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        handlers.RotatingFileHandler("HuTaoLogs.txt", mode="w+", maxBytes=1000000),
        StreamHandler(),
    ],
)
getLogger("pyrogram").setLevel(ERROR)

# --------------------------------- #

DBNAME = "HUTAO"

mongo = AsyncClient(DB_URL)
dbname = mongo[DBNAME]

# --------------------------------- #

MOD_LOAD = []
MOD_NOLOAD = []
HELPABLE = {}
start = time.time()
Hutao_Ver = "0.0.1"
TIME_ZONE = pytz.timezone(TIMEZONE)

# --------------------------------- #

# SET UP THE CLIENT
app = Client(
    "HuTao",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# START THE CLIENT AND GET INFO
app.start()
BOT_ID = "5691954374"
BOT_NAME = "Kᴏᴍɪ"
BOT_USERNAME = "TheKomi_Bot"
