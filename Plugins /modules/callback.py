from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from .. import Mukesh
from config import *
from pyrogram import filters
import re
from pyrogram.errors import UserNotParticipant
from ..database import collection, add_refer_balance, add_default_balance
from pyrogram.enums import ChatMemberStatus
# Callback handler
@Mukesh.on_callback_query()
async def callback_all(client, query: CallbackQuery):
    if query.data == 'deposit':
        await query.message.delete()
        await query.message.reply_photo(deposit_IMG, caption=desposit_text, reply_markup=buttons)

    if query.data == "INR":
        await query.message.delete()
        await query.message.reply_photo(
            INR_IMG,
            caption=f"""₹ ⤨ ᴜᴘɪ ɪᴅ 
➩  narayanpurohit444@ibl

💢 ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ

‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ꜰᴜɴᴅ ɪɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("• ʙᴀᴄᴋ •", callback_data='deposit')],
                [InlineKeyboardButton("⭒ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴsʜᴏᴛ ⭒", url="https://t.me/jn_dev")]
            ])
        )
    match = re.match(r"^(approve|reject)_(\d+)_(\d+(\.\d+)?)_(.+)$", query.data)
    # print("33",match)
    if match:
        action, user_id, amount, _, upi_id = match.groups()
        print(user_id,action,amount,_,upi_id)
        user_id = int(user_id)
        amount = float(amount)
        if action == "approve":
            await Mukesh.send_message(
                user_id,
                f"Your withdrawal request for INR {amount} has been approved."
            )
            await query.answer("Withdrawal approved.")
        else:
            collection.update_one({'user_id': user_id}, {'$inc': {'balance': amount}})
            await Mukesh.send_message(
                user_id,
                f"Your withdrawal request for INR {amount} has been rejected. The amount has been refunded to your balance."
            )
            await query.answer("Withdrawal rejected.")
    if query.data.startswith("joined"):
        datas=query.data.split("_")
        user_id=int(datas[1].replace("{","").replace("}", ""))
        referred_by=datas[-1]

        print("line 56", user_id, referred_by)
        try:
            user = await client.get_chat_member(UPDATE_CHNL, user_id)
            support = await client.get_chat_member(SUPPORT_GRP, user_id)
            # print(user)
            if user.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.OWNER,ChatMemberStatus.ADMINISTRATOR] and support.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.OWNER,ChatMemberStatus.ADMINISTRATOR]:
                await add_refer_balance(user_id=referred_by, refer_in=REFER_BONUS)
                add_default_balance(user_id=user_id)
                await client.send_message(user_id, f"Congratulations! You've received {NEW_USER_BONUS}₹ as a new user bonus.")
                await client.send_message(referred_by, f"Congratulations! You've received {REFER_BONUS}₹ for referring a new user.")
                await Mukesh.send_message(log_channel, text=f"🦋 #bonus 🦋,\n\n**ID** : {user_id}\n**Name**: {query.from_user.first_name}\n**Referred by**: {referred_by}\n**Bonuses awarded**: {NEW_USER_BONUS}₹ to new user, {REFER_BONUS}₹ to referrer")
                await query.answer("You have successfully joined the channels and received your bonus! 🎉")
            else:
                await query.answer("You need to join both the Update Channel and Support Group to receive the bonuses. hi", show_alert=True)
        except UserNotParticipant:
            await query.answer("You need to join both the Update Channel and Support Group to receive the bonuses. ❌", show_alert=True)