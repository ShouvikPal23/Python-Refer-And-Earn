# github - JNBOTS

from .. import JN
from ..database import update_balance,deposits,collection
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton

from config import *


     # profile 
@JN.on_message((filters.regex("🪪 ᴍʏ ᴘʀᴏꜰɪʟᴇ") | filters.command("Profile") )& filters.private)
async def Profile_msg(_, message):
    # print(message)
    await message.delete()
    if message.text == "🪪 ᴍʏ ᴘʀᴏꜰɪʟᴇ" or (message.command and (message.command[0] == "profile")):
        document = collection.find_one({"user_id": message.from_user.id})
        balance = document.get("balance")
        user_info = f"""
ɴᴀᴍᴇ : {message.from_user.mention}
ʙᴀʟᴀɴᴄᴇ : {round(balance,2)} INR
total refer : {document.get("total_refer")}
ᴠᴇʀꜱɪᴏɴ 1.7"""
        await message.reply_photo(photo=photo,caption=user_info)