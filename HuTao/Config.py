#MIT License
#Copyright (c) 2023, ©NovaNetworks

import sys
from logging import getLogger

LOGGER = getLogger(__name__)

# Required ENV
try:
    BOT_TOKEN = "6270655198:AAEqPMXf4jVft2pNwz58AGzzyqkrOYRBX2E" # BOT TOKEN
    API_ID = 14056295  # API ID
    API_HASH = "9ae65901d2eeb5854cc5aa562566d34a" # API HASH
except Exception as e:
    LOGGER.error(f"Looks Like Something Is Missing!! Please Check Variables\n{e}")
    sys.exit(1)


TIMEZONE = "Asia/Kolkata" # YOUR TIME ZONE

COMMAND_HANDLER = ". /".split() # COMMAND HANDLER

SUDO = list({int(x)for x in ("").split()})

SUPPORT_CHAT = "NovaSupports" # SUPPORT GROUP (ID OR USERNAME)

LOG_CHANNEL_ID = -1001816188874 #LOG GROUP ID FOR YOUR BOT

OWNER = list({int(x)for x in ("1805959544").split()}) #OWNER ID

DB_URL = "" # MONGO DB URL

SQL_URL = "" # ELEPHANT SQL URL
