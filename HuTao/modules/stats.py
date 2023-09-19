from HuTao import app, dbname
from pyrogram import filters
from pyrogram.types import Message
from HuTao.database.users_db import Users  # Import the Users class

usrdb = dbname["users"]

@app.on_message(filters.command("stats") & filters.private)
async def get_stats(_, message: Message):
    total_users = await Users.count_users(usrdb)  # Pass the database instance to count_users

    stats_message = f"**Total Users: {total_users}**"

    await message.reply_text(stats_message)

class Users:
    @staticmethod
    async def count_users(db):
        count = await db.count_documents({})  # Count the user documents in the database
        return count
