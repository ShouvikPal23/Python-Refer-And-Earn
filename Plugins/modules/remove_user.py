from .. import JN
from pyrogram import filters
from ..database import collection
from config import OWNER_ID
# Define a function to handle the /delete command
@JN.on_message(filters.command("delete") & filters.private)
async def delete_command_handler(bot, message):   
    if message.from_user.id == OWNER_ID:
        if len(message.command) == 2:
            user_id_to_delete = int(message.command[1])
            # Check if the user exists in the database
            if collection.find_one({'user_id': user_id_to_delete}):
                # Delete the user from the database
                collection.delete_one({'user_id': user_id_to_delete})
                await message.reply(f"User with ID {user_id_to_delete} has been deleted from the database.")
            else:
                await message.reply("User not found in the database.")
        else:
            await message.reply("Please provide the user ID to delete.")
    else:
        await message.reply("You are not authorized to use this command.")