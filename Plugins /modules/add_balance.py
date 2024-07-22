from .. import Mukesh
from ..database import update_balance, deposits,collection
from pyrogram import filters
from config import OWNER_ID

@Mukesh.on_message(filters.command("add"),group=7)
async def handle_message(client, message):
    # print(message)
    if message.from_user.id==int(OWNER_ID):
    # if message.command[0].lower() == 'add':
        msg1 = await Mukesh.ask(int(OWNER_ID), "How much money do you want to add? Please provide amount in INR format.")
        amount = float(msg1.text)
        print(amount)
        msg2 = await Mukesh.ask(int(OWNER_ID), "Please provide the user ID to whom you want to add money.")
        user_id = int(msg2.text)
        print(user_id)
        response = await deposits(user_id, amount)
        await client.send_message(int(OWNER_ID), response)
        await client.send_message(user_id, response)
        document = collection.find_one({"user_id": user_id})
        total_deposit=document.get('total_deposits', 0)+amount
        if document:
            collection.update_one(document,{'$set': {'total_deposits':total_deposit}})
        
    else:
        await client.reply("You are not authorized to use this command.")
