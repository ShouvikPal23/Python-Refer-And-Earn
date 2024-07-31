import os
from pyrogram.types import KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton,WebAppInfo,ReplyKeyboardMarkup

#get from https://my.telegram.org/auth
API_ID:int =(os.environ.get("API_ID",21714374))
API_HASH:str = os.environ.get("API_HASH", "700092e37d7da9a7b781994b7503a488")
BOT_TOKEN:str = os.environ.get("BOT_TOKEN", "6909761308:AAFpefO5KpfOHfKKjUQeZX7bjoEMPWg4jsE")


REFER_BONUS=int(1)
NEW_USER_BONUS=int(1)

#username without @
UPDATE_CHNL:str = os.environ.get("UPDATE_CHNL", "jn_bots")
SUPPORT_GRP:str = os.environ.get("SUPPORT_GRP", "jn_smm")
BOT_USERNAME:str = os.environ.get("BOT_USERNAME", "JN_SMM_BOT")

#get it from @username_to_id_bot this bot 

log_channel = int(os.environ.get("LOG_CHANNEL", "-1001918482012"))
OWNER_ID=int(os.environ.get("OWNER_ID",5597521952))


# search on youtube "how to create mongodburl""

MONGO_DB_URI:str = os.environ.get(
    "MONGO_DB_URI",
    "mongodb+srv://rajpriti712:NHAvrha6XNd043uI@cluster0.a9pzur5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	


INR_IMG="https://graph.org/file/591e034f3ebaca25e0692.jpg"
START_IMG= "https://graph.org/file/877838e68ea8e3099f343.jpg"
start_img2="https://graph.org/file/e1f08dea685a9051b264c.jpg"
photo="https://graph.org/file/8e2df166f47509590c88e.jpg"
deposit_IMG="https://graph.org/file/d46f6efe8fe5c991491ed.jpg"



                
desposit_text=f"""

🖥 Dᴇᴘᴏsɪᴛ Pʟᴀɴs
ᴏꜰꜰᴇʀ ᴠᴀʟɪᴅ ᴜᴘ ᴛᴏ 17/04/2024
**🎉30% ʙᴏɴᴜꜱ +**
⚡️ 𝟷 Rs: Nᴏ Vɪᴇᴡs Bᴏɴᴜs
⚡️𝟷𝟶 Rs: 1k Vɪᴇᴡs Bᴏɴᴜs
⚡️𝟹𝟶 Rs: 4k Vɪᴇᴡs Bᴏɴᴜs
⚡️𝟻𝟶 Rs: 7k Vɪᴇᴡs Bᴏɴᴜs
⚡️𝟷𝟶𝟶 Rs: 15k Vɪᴇᴡs Bᴏɴᴜs 
⚡️ 200 Rs: 35K Vɪᴇᴡs Bᴏɴᴜs
⚡️ 500 Rs: 80ᴋ Vɪᴇᴡs Bᴏɴᴜs
⚡️ 1000: Rs 200ᴋ Vɪᴇᴡs Bᴏɴᴜs

💙"""
buttons = InlineKeyboardMarkup([[InlineKeyboardButton("• ᴘᴀʏ ᴡɪᴛʜ ᴜᴘɪ •", callback_data='INR')
]])

main_button = ReplyKeyboardMarkup(
        [
            [KeyboardButton("🪪 ᴍʏ ᴘʀᴏꜰɪʟᴇ"), KeyboardButton("🤑 ꜰʀᴇᴇ ᴍᴏɴᴇʏ 🤑")],
            [KeyboardButton("⚡️ ᴡɪᴛʜᴅʀᴀᴡᴀʟ ⚡️"), KeyboardButton("💸 ᴀᴅᴅ ꜰᴜɴᴅ")], 
            [KeyboardButton("ᴄʀᴇᴀᴛᴏʀ 😉", web_app=WebAppInfo(url="https://jnbots.netlify.app"))]
        ],
        resize_keyboard=True
    )

all_platform = ReplyKeyboardMarkup(
        [
        [KeyboardButton("❤️‍🔥 ʀᴇꜰᴇʀ ᴀɴᴅ ᴇᴀʀɴ"), KeyboardButton("ᴅɪᴄᴇ ɢᴀᴍᴇ 🥳")],
            [KeyboardButton("⚽️ ꜰᴏᴏᴛʙᴀʟʟ "), KeyboardButton("ᴄᴏʟᴏʀ ᴘʀᴇᴅɪᴄᴛɪᴏɴ 🎱")],
            [ KeyboardButton("〄 ᴍᴀɪɴ ᴍᴇɴᴜ 〄")]
        ],
        resize_keyboard=True
    )

