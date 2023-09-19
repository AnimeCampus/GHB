from HuTao import app, dbname
from pyrogram import filters
from pyrogram.types import Message
from HuTao.database.users_db import Users
from HuTao.Config import OWNER

usrdb = dbname["users"]

@app.on_message(filters.command(["stats", "users"]))
async def get_stats(_, message: Message):
    user_id = message.from_user.id

    if user_id not in OWNER:
        await message.reply_text("You are not authorized to use this command.")
        return

    total_users = await Users.count_users(usrdb)

    stats_message = f"**Total Users: {total_users}**"

    await message.reply_text(stats_message)

class Users:
    @staticmethod
    async def count_users(db):
        count = await db.count_documents({})
        return count
