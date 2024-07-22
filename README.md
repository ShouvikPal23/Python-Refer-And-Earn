<h1 align="center">SMM panel Bot</h1>

<p align="center">
<a href="https://github.com/Noob-Mukesh/smm-panel/stargazers"><img src="https://img.shields.io/github/stars/Noob-Mukesh/smm-panel?color=black&logo=github&logoColor=black&style=for-the-badge" alt="Stars" /></a>
<a href="https://github.com/Noob-Mukesh/smm-panel/network/members"> <img src="https://img.shields.io/github/forks/Noob-Mukesh/smm-panel?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>
<a href="https://github.com/Noob-Mukesh/smm-panel/blob/master/LICENSE"> <img src="https://img.shields.io/badge/License-MIT-blueviolet?style=for-the-badge" alt="License" /> </a>
<a href="https://www.python.org/"> <img src="https://img.shields.io/badge/Written%20in-Python-skyblue?style=for-the-badge&logo=python" alt="Python" /> </a>

<a href="https://pypi.org/project/Pyrogram/"> <img src="https://img.shields.io/pypi/v/pyrogram?color=white&label=pyrogram&logo=python&logoColor=blue&style=for-the-badge" /></a>
<a href="https://github.com/Noob-Mukesh/smm-panel"> <img src="https://img.shields.io/github/repo-size/Noob-Mukesh/smm-panel?color=skyblue&logo=github&logoColor=blue&style=for-the-badge" /></a>
<a href="https://github.com/Noob-Mukesh/smm-panel/commits/Noob-Mukesh "> <img src="https://img.shields.io/github/last-commit/Noob-Mukesh/smm-panel?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>

</p>

━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━

<h2 align="center"> 
    ʀᴇǫᴜɪʀᴇᴍᴇɴᴛs 
</h2>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-3120/"> ᴘʏᴛʜᴏɴ 3.12.0 </a> |
    <a href="https://docs.pyrogram.org/intro/setup#api-keys"> ᴛᴇʟᴇɢʀᴀᴍ ᴀᴘɪ ᴋᴇʏ </a> |
    <a href="https://t.me/botfather"> ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏᴋᴇɴ </a> | 
    <a href="https://telegra.ph/How-To-get-Mongodb-URI-04-06"> ᴍᴏɴɢᴏᴅʙ ᴜʀɪ </a>
</p>
━━━━━━━━━━━━━━━━━━━━

<h2>  ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ​ 🚀</h2> 
ᴛʜᴇ ᴇᴀsɪᴇsᴛ ᴡᴀʏ ᴛᴏ ᴅᴇᴘʟᴏʏ 
<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/noob-mukesh/smm-panel"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>
 ━━━━━━━━━━━━━━━━━━━━━━

<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ᴠᴘs/ʟᴏᴄᴀʟ 」─
</h3>

<h3>
- <b> ᴠᴘs/ʟᴏᴄᴀʟ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ </b>
</h3>

- Get your [Necessary Variables](https://github.com/Noob-Mukesh/smm-panel/blob/main/smm-panel/config.py)
- Upgrade and Update by :
  `sudo apt-get update && sudo apt-get upgrade -y`
- Install required packages by :
  `sudo apt-get install python3-pip -y`
- Install pip by :
  `sudo pip3 install -U pip`
- Clone the repository by :
  `git clone https://github.com/Noob-Mukesh/smm-panel && cd smm-panel`
- Install/Upgrade setuptools by :
  `pip3 install --upgrade pip setuptools`
- Install requirements by :
  `pip3 install -U -r requirements.txt`
- Fill your variables in config by :
  `vi smm/config.py`

Press `I` on the keyboard for editing config

Press `Ctrl+C` when you're done with editing config and `:wq` to save the config

- Install tmux to keep running your bot when you close the terminal by :
  `sudo apt install tmux && tmux`
- Finally run the bot by :
  `python3 -m smm`
- For getting out from tmux session

Press `Ctrl+b` and then `d`

━━━━━━━━━━━━━━━━━━━━

<h2 align="center"> 
    ᴡʀɪᴛᴇ ɴᴇᴡ ᴍᴏᴅᴜʟᴇs 
</h2>

```py
#ᴀᴅᴅ ʟɪᴄᴇɴsᴇ ᴛᴇxᴛ ʜᴇʀᴇ ɢᴇᴛ ɪᴛ ғʀᴏᴍ ʙᴇʟᴏᴡ.

from .. import  Mukesh # This is bot's client
from pyrogram import filters # pyrogram filters



#ғᴏʀ /help ᴍᴇɴᴜ
__mod_name__ = "Module Name"
__help__ = "Module help message"


@Mukesh.on_message(filters.command("start"))
async def some_function(_, message):
    await message.reply_text("ɪ'ᴍ.ᴀʟɪᴠᴇ ʙᴀʙʏ❣️!!")

# ᴍᴀɴʏ ᴜsᴇғᴜʟ ғᴜɴᴄᴛɪᴏɴs ᴀʀᴇ ɪɴ, smm-panel/utils/,smm-panel, and smm-panel/modules/
```

<h3 align="center"> 
 ᴀɴᴅ ᴘᴜᴛ ᴛʜɪs ғɪʟᴇ ɪɴ smm/modules/, ʀᴇsᴛᴀʀᴛ ᴀɴᴅ ᴛᴇsᴛ ʏᴏᴜʀ ʙᴏᴛ.
</h3>

━━━━━━━━━━━━━━━━━━━━

<h3 align="center">
    ─「 sᴜᴩᴩᴏʀᴛ 」─
</h3>

<p align="center">
<a href="https://telegram.me/the_support_chat"><img src="https://img.shields.io/badge/-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>
<p align="center">
<a href="https://telegram.me/mukeshbotzone"><img src="https://img.shields.io/badge/-Support%20Channel-blue.svg?style=for-the-badge&logo=telegram"></a>
</p>

━━━━━━━━━━━━━━━━━━━━

### ㅤㅤㅤㅤᴄʀᴇᴅɪᴛs

[ ᴍᴜᴋᴇsʜ ](https://t.me/mr_sukkun)

<b>ᴀɴᴅ ᴀʟʟ [ᴛʜᴇ ᴄᴏɴᴛʀɪʙᴜᴛᴏʀs](https://github.com/Noob-Mukesh/smm-panel/graphs/contributors) ᴡʜᴏ ʜᴇʟᴩᴇᴅ ɪɴ ᴍᴀᴋɪɴɢ ᴜsᴇғᴜʟ & ᴩᴏᴡᴇʀғᴜʟ ❤️ </b>

━━━━━━━━━━━━━━━━━━━━
