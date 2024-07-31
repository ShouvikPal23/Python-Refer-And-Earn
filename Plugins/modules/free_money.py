from pyrogram import filters, Client
import asyncio
from .. import JN
from pyrogram.enums import ParseMode
from pyrogram.errors import UserNotParticipant, ChatWriteForbidden, ChatAdminRequired
from config import UPDATE_CHNL, SUPPORT_GRP as Update2,START_IMG,all_platform

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@JN.on_message(filters.regex('🤑 ꜰʀᴇᴇ ᴍᴏɴᴇʏ 🤑') & filters.private)
async def must_join_channel(bot: Client, msg):
    await msg.reply("**ᴘʟᴇᴀꜱᴇ ꜱᴇʟᴇᴄᴛ ᴏᴘᴛɪᴏɴ:**\n\nɪɴ ʀᴇꜰᴇʀ ᴀɴᴅ ᴇᴀʀɴ ʏᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ʙʏ ɪɴᴠɪᴛᴇ ᴜꜱᴇʀ\n\nɪɴ ᴏᴛʜᴇʀꜱ ᴏᴘᴛɪᴏɴꜱ ʏᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ʙʏ ʙᴇᴛᴛɪɴɢ.", reply_markup=all_platform)
    
@JN.on_message(filters.regex('📍ᴄᴀɴᴄᴇʟ ʙᴇᴛ📍') & filters.private)
async def must_join_channel(bot: Client, msg):
    await msg.reply("**ᴘʟᴇᴀꜱᴇ ꜱᴇʟᴇᴄᴛ ᴏᴘᴛɪᴏɴ:**\n\nɪɴ ʀᴇꜰᴇʀ ᴀɴᴅ ᴇᴀʀɴ ʏᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ʙʏ ɪɴᴠɪᴛᴇ ᴜꜱᴇʀ\n\nɪɴ ᴏᴛʜᴇʀꜱ ᴏᴘᴛɪᴏɴꜱ ʏᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ʙʏ ʙᴇᴛᴛɪɴɢ.", reply_markup=all_platform)