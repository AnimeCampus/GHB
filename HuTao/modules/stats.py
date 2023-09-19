import HuTao.Config
import platform
import time
import datetime
from HuTao import app, dbname
from pyrogram import filters , Client
from platform import python_version
from HuTao.Config import SUDO as SUPREME_USERS
from psutil import boot_time, cpu_percent, disk_usage, virtual_memory
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup


@Client.on_message(filters.command('stats'))
async def _stats(client,message):
     if message.from_user.id not in SUPREME_USERS:
          return
     status = "** 「 Bot Statistics: 」**\n\n"
     status += f'**• Total Chats :** `{await db.chats.count_documents({})}`\n'
     status += f'**• Total Users :** `{await db.users.count_documents({})}`\n'   
     await message.reply_text(status,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Close",callback_data='close')]]))
    
