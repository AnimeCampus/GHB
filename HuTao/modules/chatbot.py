import os
import requests
import json
import asyncio
from HuTao import app, BOT_USERNAME, BOT_ID, BOT_NAME, dbname
from pyrogram import filters, enums, Client
from pyrogram.types import Message , InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery 
from HuTao.database.chat_actions import send_action
from HuTao.database.chatbot_db import chatbotdb, addchat_bot, rmchat_bot


# Define inline keyboard buttons
buttons = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="Enable", callback_data="add_chat"),
      InlineKeyboardButton(text="Disable", callback_data="rm_chat")]]
)

# Define chat actions for typing
async def send_typing_action(_, chat_id):
    await _.send_chat_action(chat_id, enums.ChatAction.TYPING)

# Check if a message is addressed to the bot
async def is_bot_mention(_, message):
    if BOT_USERNAME in message.text:
        return True
    return False

# Command to enable/disable chatbot
@app.on_message(filters.command("chatbot"))
async def chatbot_command(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if message.chat.type != enums.ChatType.PRIVATE:
        chat_member = await app.get_chat_member(chat_id, user_id)
        if chat_member.status in ("administrator", "creator"):
            await message.reply_text("**Choose an option.**", reply_markup=buttons)
        else:
            await message.reply_text("**You need to be an admin to use this command.**")
    else:
        await message.reply_text("**Choose an option.**", reply_markup=buttons)

# Callback to enable chatbot
@app.on_callback_query(filters.regex("add_chat"))
async def enable_chatbot(_, query):
    chat_id = query.message.chat.id
    check_chat = await chatbotdb.find_one({"chat_id": chat_id})

    if query.message.chat.type != enums.ChatType.PRIVATE:
        chat_member = await app.get_chat_member(chat_id, query.from_user.id)
        if chat_member.status in ("administrator", "creator"):
            if not check_chat:
                await addchat_bot(chat_id)
                await query.message.edit_caption("**Enabled Chatbot in This Chat!**")
            else:
                await query.message.edit_caption("**Chatbot is already enabled in this chat.**")
        else:
            await query.answer(text="You can't do that.", show_alert=True)
    else:
        if not check_chat:
            await addchat_bot(chat_id)
            await query.message.edit_caption("**Enabled Chatbot in This Chat!**")
        else:
            await query.message.edit_caption("**Chatbot is already enabled in this chat.**")

# Callback to disable chatbot
@app.on_callback_query(filters.regex("rm_chat"))
async def disable_chatbot(_, query):
    chat_id = query.message.chat.id
    check_chat = await chatbotdb.find_one({"chat_id": chat_id})

    if query.message.chat.type != enums.ChatType.PRIVATE:
        chat_member = await app.get_chat_member(chat_id, query.from_user.id)
        if chat_member.status in ("administrator", "creator"):
            if check_chat:
                await rmchat_bot(chat_id)
                await query.message.edit_caption("**Disabled Chatbot in This Chat!**")
            else:
                await query.message.edit_caption("**Chatbot is already disabled in this chat.**")
        else:
            await query.answer(text="You can't do that.", show_alert=True)
    else:
        if check_chat:
            await rmchat_bot(chat_id)
            await query.message.edit_caption("**Disabled Chatbot in This Chat!**")
        else:
            await query.message.edit_caption("**Chatbot is already disabled in this chat.**")

# Function to handle chatbot messages
async def handle_chatbot_message(_, message):
    chat_id = message.chat.id
    check_chat = await chatbotdb.find_one({"chat_id": chat_id})

    if not check_chat:
        return

    if message.text and not message.document:
        if not await is_bot_mention(_, message):
            return

        await send_typing_action(_, chat_id)
        url = f"https://api.safone.me/chatbot?query={message.text}&user_id=69&bot_name=itachi%20uchiha&bot_master=alpha"
        results = requests.get(url).json()
        await asyncio.sleep(0.5)
        to_reply = results["response"]

        # Modify the response if needed
        if "safone" in to_reply.lower():
            to_reply = to_reply.replace("Safone", "⏤͟͞ 𝙉𝘼𝙉𝙊™ 🇮🇳")
            to_reply = to_reply.replace("t.me/asmsafone", "t.me/GenXNano")

        await message.reply_text(to_reply)

# Register the chatbot message handler
app.add_handler(handle_chatbot_message, filters.text & ~filters.bot & ~filters.via_bot, group=9)

   
__mod__ = "CHATBOT"
__help__ = """
**» /chatbot** - To activate chatbot 
"""
