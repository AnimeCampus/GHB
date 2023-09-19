import HuTao.Config
import platform
import time
import datetime
from HuTao import app, dbname
from HuTao.database.users_db import *
from pyrogram import filters , Client
from platform import python_version
from HuTao.Config import SUDO 
from psutil import boot_time, cpu_percent, disk_usage, virtual_memory
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram.types import Message

@app.on_message(filters.command("stats") & filters.private)
async def get_stats(_, message: Message):
    total_users = await Users.count_users()

    stats_message = f"**Total Users: {total_users}**"

    await message.reply_text(stats_message)

class Users:
    @staticmethod
    async def count_users():
        count = await usrdb.count_documents({})
        return count
