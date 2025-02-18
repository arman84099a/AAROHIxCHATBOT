from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re
import asyncio
import time
from datetime import datetime
#from database.users_chats_db import db

API_ID = "14050586"
API_HASH = "42a60d9c657b106370c79bb0a8ac560c"
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
MONGO_URL = ("MONGO_URL","mongodb+srv://Arman121:Arman121@arman.ji8gqxd.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME") 
BOT_USERNAME = os.environ.get("BOT_USERNAME")
BOT_NAME = os.environ.get("BOT_NAME")
ADMINS = os.environ.get("ADMINS")

bot = Client(
    "SʜʀᴇᴇCʜᴀᴛBᴏᴛ" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


EMOJIOS = [ 
      "❤",
      "💖",
]
      
START = f"""
**๏ Hie Baby❣️ ๏**
"""

@bot.on_message(filters.command(["start", "aistart", f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
    accha = await m.reply_text(
                text = random.choice(EMOJIOS),
    )
    await asyncio.sleep(1)
    await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠..")
    await asyncio.sleep(0.1)
    await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠...")
    await asyncio.sleep(0.1)
    await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠....")
    await asyncio.sleep(0.1)
    await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐞𝐝.✓")
    await asyncio.sleep(0.2)
    await accha.edit("𝙷ᴇʟʟᴏ ɢᴜʏs ᴛʜɪs ɪs ❥≛⃝🥀sʜʀᴇᴇ ᴀʀᴍᴀɴ ᴋɪ ᴊᴀᴀɴ』⃝⛓️❤️. ᴡʜɪᴄʜ ɪs ᴡʀɪᴛᴛᴇɴ ɪɴ ᴘʏʀᴏɢʀᴀᴍ...ʏᴏᴜ ᴄᴀɴ ʏᴏᴜ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴀs ᴀ ᴄʜᴀᴛ ʙᴏᴛ...sᴜᴘᴘᴏʀᴛ :- @Dil_Ka_Ehsaas ")
       
@bot.on_message(
    filters.command(["chatbot off", f"chatbot@{BOT_USERNAME} off"], prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    Sʜʀᴇᴇdb = MongoClient(MONGO_URL)    
    sʜʀᴇᴇ = Sʜʀᴇᴇdb["Sʜʀᴇᴇdb"]["Sʜʀᴇᴇ"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "You are not admin"
            )
    is_sʜʀᴇᴇ = sʜʀᴇᴇ.find_one({"chat_id": message.chat.id})
    if not is_aarohi:
        sʜʀᴇᴇ.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"Chatbot Disabled!")
    if is_sʜʀᴇᴇ:
        await message.reply_text(f"ChatBot Already Disabled")
    

@bot.on_message(
    filters.command(["chatbot on", f"chatbot@{BOT_USERNAME} on"] ,prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    Sʜʀᴇᴇdb = MongoClient(MONGO_URL)    
    sʜʀᴇᴇ = Sʜʀᴇᴇdb["AarohiDb"]["Sʜʀᴇᴇ"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_sʜʀᴇᴇ = sʜʀᴇᴇ.find_one({"chat_id": message.chat.id})
    if not is_sʜʀᴇᴇ:           
        await message.reply_text(f"Chatbot Already Enabled")
    if is_sʜʀᴇᴇ:
        sʜʀᴇᴇ.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"ChatBot Enabled!")
    

@bot.on_message(
    filters.command(["chatbot", f"chatbot@{BOT_USERNAME}"], prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**ᴜsᴀɢᴇ:**\n/**chatbot [on/off]**\n**ᴄʜᴀᴛ-ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ(s) ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!**")


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def sʜʀᴇᴇai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       sʜʀᴇᴇdb = MongoClient(MONGO_URL)
       sʜʀᴇᴇ = Sʜʀᴇᴇdb["SʜʀᴇᴇDb"]["Sʜʀᴇᴇ"] 
       is_sʜʀᴇᴇ = sʜʀᴇᴇ.find_one({"chat_id": message.chat.id})
       if not is_sʜʀᴇᴇ:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       Sʜʀᴇᴇdb = MongoClient(MONGO_URL)
       sʜʀᴇᴇ = Sʜʀᴇᴇdb["SʜʀᴇᴇDb"]["Sʜʀᴇᴇ"] 
       is_sʜʀᴇᴇ = sʜʀᴇᴇ.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_sʜʀᴇᴇ:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def sʜʀᴇᴇstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       Sʜʀᴇᴇdb = MongoClient(MONGO_URL)
       sʜʀᴇᴇ = Sʜʀᴇᴇdb["SʜʀᴇᴇDb"]["Sʜʀᴇᴇ"] 
       is_sʜʀᴇᴇ = sʜʀᴇᴇ.find_one({"chat_id": message.chat.id})
       if not is_sʜʀᴇᴇ:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       Sʜʀᴇᴇdb = MongoClient(MONGO_URL)
       sʜʀᴇᴇ = Sʜʀᴇᴇdb["SʜʀᴇᴇDb"]["Sʜʀᴇᴇ"] 
       is_sʜʀᴇᴡ = sʜʀᴇᴇ.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_sʜʀᴇᴇ:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def sʜʀᴇᴇprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def sʜʀᴇᴇprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")

print(f"❣️𝗦𝗛𝗥𝗘𝗘 𝗖𝗛𝗔𝗧𝗕𝗢𝗧💝𝗜𝗦 𝗦𝗧𝗔𝗥𝗧𝗘𝗗❣️ ")      
bot.run()
