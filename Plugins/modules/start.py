from datetime import date as date_
import datetime
from .. import Mukesh
from pyrogram import filters
from ..database import collection, add_default_balance, is_new_user
from config import start_img2, main_button,log_channel,START_IMG
import asyncio
import time
start_img2="https://graph.org/file/e1f08dea685a9051b264c.jpg"

currentTime = datetime.datetime.now()

testhour=currentTime

if 23 <=currentTime.hour < 5:
    wish = "❤️ **Good morning **❤️"
elif 5 <= currentTime.hour < 11:
    wish = '🤍 **Good afternoon **🤍'
elif 11 <= currentTime.hour < 14:
    wish = '🦋 **Good evening **🦋'
else:
    wish = '💖 **Good night** 💖'



# Define a function to handle the /start command
@Mukesh.on_message(filters.command("START") & filters.private)
async def start_command_handler(b, m):
    caption = f"Hello {m.from_user.first_name}, \nI'm {Mukesh.mention}\n\n"\
                  "I'm a powerful SMM bot. You can buy any type of SMM service here.\n\n"\
                  "Maintained by: <a href='https://t.me/jn_dev/'>JN Dev</a>"
    caption2 = f"Hello {m.from_user.first_name},\n\n ʜᴇʏ ʟᴏᴏᴋ ʟɪᴋᴇ ʏᴏᴜ ᴀʀᴇ ɴᴇᴡ ʜᴇʀᴇ ᴏɴᴇ ʟɪᴛᴛʟᴇ ɢɪꜰᴛ ꜰʀᴏᴍ ᴍᴇ ʏᴏᴜ ᴊᴜꜱᴛ ɢᴏᴛ +1 ₹ ᴀꜱ ʙᴏɴᴜꜱ.\n\nʀᴜɴ ᴛʜᴇ /start ᴄᴏᴍᴍᴀɴᴅ ᴀɢᴀɪɴ ᴛᴏ ꜱᴛᴀʀᴛ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ."

    # Check if the user is new
    if is_new_user(m.from_user.id):
        # Add the user to the database and give them a welcome message
        add_default_balance(m.from_user.id)

        j=await m.reply_sticker("CAACAgUAAxkDAAIIImYMPfDBC9C0hwEdm34oVxFYbAYLAAJrDgACIHkgVAjUFXHyK3urHgQ")
        await asyncio.sleep(1)
        await j.delete()
        await Mukesh.send_photo(m.chat.id, photo=start_img2, caption=caption, reply_markup=main_button)
        await Mukesh.send_message(m.chat.id, text="Hey you just got +1₹ in your acount as new user bonus  ")
        await Mukesh.send_message(log_channel, text=f"🦋 #newuser 🦋,\n\n**ID** : `{m.from_user.id}`\n**Name**: {m.from_user.first_name}\n **refer by:**No one    ")



    else:
        # User already exists, send the regular start message
        j=await m.reply_sticker("CAACAgUAAxkBAAECPc9mA9nqb8a0d0ziqad0mrNlleIXXAAC0w4AAudpIVTD64tNd-x1Xx4E")
        await asyncio.sleep(1)
        await j.delete()


        j=await m.reply_sticker("CAACAgUAAxkBAAECPcpmA9bYkPLWQz9DGg0KL5tShE3QRwACrQ8AAutgIVRELBWrQpHOux4E")
        await asyncio.sleep(1)
        await j.delete()
        j=await Mukesh.send_photo(m.chat.id, photo=start_img2, caption=caption, reply_markup=main_button)




@Mukesh.on_message(filters.regex('〄 ᴍᴀɪɴ ᴍᴇɴᴜ 〄') & filters.private)
async def main_menu_handler(bot, message):

    caption = f"Hello {message.from_user.first_name},\n\nI'm a powerful SMM bot. You can buy any type of SMM service here.\n\nMaintained by: <a href='https://t.me/jn_dev/'>JN Dev</a>"

    await Mukesh.send_photo(message.chat.id, photo=start_img2, caption=caption, reply_markup=main_button)
    await message.delete()