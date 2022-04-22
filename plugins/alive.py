import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/1ce8ad1f3d7d44b19f207.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥Add me to your group and enjoy the high quality songs over telegram video chat feature. 
┏━━━━━━━━━━━━━━━━━┓
┣★ Developer : [Aditya](https://t.me/near44)
┣★ Manager : [♛┈⛧┈┈•༶ØP Gírl༶•┈┈⛧┈♛](https://t.me/OP_Girll)
┣★ Support : [✰ 𝐅𝐫𝐢𝐞𝐧𝐝𝐬 𝐅𝐨𝐫𝐞𝐯𝐞𝐫 ✰](https://t.me/OP_FRlENDS)
┣★ Chat : [✿❀Aɴɪᴍᴇ Wᴏʀʟᴅ❀✿](https://t.me/ANIME_WORLD15)
┗━━━━━━━━━━━━━━━━━┛

💞 Dot forget to join our groups for further updates.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴊᴏɪɴ ʜᴇʀᴇ ғᴏʀ ᴜᴘᴅᴀᴛᴇs ❱ ➕", url=f"https://t.me/OP_FRlENDS")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "aditya", "near"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/b0cbf256b34584cce041a.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ 💞", url=f"https://t.me/OP_FRlENDS")
                ]
            ]
        ),
    )

