  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
import os
import requests
import json
import asyncio
from HuTao import app, BOT_USERNAME, BOT_ID, BOT_NAME, dbname
from pyrogram import filters, enums, Client
from pyrogram.types import Message , InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery 
from HuTao.database.chat_actions import send_action
from HuTao.database.chatbot_db import chatbotdb, addchat_bot, rmchat_bot


buttons = InlineKeyboardMarkup([[ InlineKeyboardButton(text="Enable", callback_data="add_chat"),InlineKeyboardButton(text="Disable", callback_data="rm_chat")]])  

@Client.on_message(filters.command("chatbot"))
async def _check_bot(_, message):
    if message.sender_chat:
        return
    chat_id = message.chat.id
    user_id = message.from_user.id
    if message.chat.type != enums.ChatType.PRIVATE:
        xx = await _.get_chat_member(chat_id,user_id)
        if xx.privileges:           
            return await message.reply_text("Choose An Option.",reply_markup=buttons)
        else:
            return await message.reply_text("You need to be admin to use this command.")
    else:
        return await message.reply_text("Choose An Option.",reply_markup=buttons)
    

@Client.on_callback_query(filters.regex("add_chat"))
async def _addchat(app : Client, query : CallbackQuery):
    user_id = query.from_user.id
    chat_id = query.message.chat.id
    check_chat = await chatbotdb.find_one({"chat_id" : chat_id})
    if query.message.chat.type != enums.ChatType.PRIVATE:
        
        xx = await app.get_chat_member(chat_id,user_id)
        if xx.privileges:    
            if not check_chat:  
                await addchat_bot(chat_id)           
                return await query.message.edit_caption("Enabled Chatbot in This Chat!")      
                
            elif check_chat:
                await query.message.edit_caption("Chatbot is already enabled in this chat.")
            
   
        else:
            await client.answer_callback_query(
            query.id,
            text = "You can't do that.",
            show_alert = True)
    else:
        if not check_chat:
            await addchat_bot(user_id)                     
            return await query.message.edit_caption("Enabled Chatbot in This Chat!") 
        elif check_chat:
            await query.message.edit_caption("Chatbot is already enabled in this chat.")   
             
@Client.on_callback_query(filters.regex("rm_chat"))
async def _rmchat(app : Client, query : CallbackQuery):
    user_id = query.from_user.id
    chat_id = query.message.chat.id
    check_chat = await chatbotdb.find_one({"chat_id" : chat_id})
  
    if query.message.chat.type != enums.ChatType.PRIVATE:
        xx = await app.get_chat_member(chat_id,user_id)
        if xx.privileges:    
            if check_chat:  
                await rmchat_bot(chat_id)           
                return await query.message.edit_caption("Disabled Chatbot in This Chat!")      
                
            elif not check_chat:
                await query.message.edit_caption("Chatbot is already disabled in this chat.**")
            
   
        else:
            await client.answer_callback_query(
            query.id,
            text = "You can't do that.",
            show_alert = True)
    else:
        if check_chat:
            await rmchat_bot(user_id)                     
            return await query.message.edit_caption("Disabled Chatbot in This Chat!") 
        elif not check_chat:
            await query.message.edit_caption("Chatbot is already disabled in this chat.")   
                 


async def itachi_message(message : Message):
    reply_message = message.reply_to_message
    if message.text.lower() == "itachi":
        return True
    elif BOT_USERNAME in message.text.upper():
        return True
    elif reply_message:
        if reply_message.from_user.id == BOT_ID:
            return True
    else:
        return False
