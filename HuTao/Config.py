#MIT License
#Copyright (c) 2023, ©NovaNetworks

import sys
from logging import getLogger

LOGGER = getLogger(__name__)

# Required ENV
try:
    BOT_TOKEN = "5691954374:AAFxuqGhI_uuCrgtHmXGyfL2HuLNClzoeDI" # BOT TOKEN
    API_ID = 14056295  # API ID
    API_HASH = "9ae65901d2eeb5854cc5aa562566d34a" # API HASH
except Exception as e:
    LOGGER.error(f"Looks Like Something Is Missing!! Please Check Variables\n{e}")
    sys.exit(1)


TIMEZONE = "Asia/Kolkata" # YOUR TIME ZONE

COMMAND_HANDLER = ". /".split() # COMMAND HANDLER

SUDO = list({int(x)for x in ("").split()})

SUPPORT_CHAT = "NanoSTestingArea" # SUPPORT GROUP (ID OR USERNAME)

LOG_CHANNEL_ID = -1001949829830 #LOG GROUP ID FOR YOUR BOT

OWNER = list({int(x)for x in ("6198858059").split()}) #OWNER ID

DB_URL = "mongodb+srv://sukuna:fazaljuly2@sukuna.vipbn9a.mongodb.net/?retryWrites=true&w=majority" # MONGO DB URL

SQL_URL = "postgres://lrorrkxn:QvwXgB1bmq536gN4qSyhcowj98XGSsfT@arjuna.db.elephantsql.com/lrorrkxn" # ELEPHANT SQL URL
