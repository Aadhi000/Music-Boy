import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bff8d2c2ba43449adbc99.jpg",
        caption=f"""**ππ·πΈπ πΈπ π°π½ π°π³ππ°π½π²π΄π³ ππ΄π»π΄πΆππ°πΌ πΌπππΈπ² π±πΎπ πππ½π πΎπ½ πΏππΈππ°ππ΄ ππΏπ ππΈππ· π·πΈπΆπ· πππ°π»πΈππ πΌπππΈπ² π°π½π³ πππΏπ΄π ππΏπ΄π΄π³.π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ πΌπ°πΊπ΄ πΌπ΄ π°π³πΌπΈπ½ ππ·π΄π½ ππ΄π°ππ²π· ππΎππ π΅π°ππΎππΈππ΄ ππΎπ½πΆπ ππΈππ· π²πΎπΌπΌπ°π½π³...//

β£βͺΌ πππΏπΏπΎππ :- [πΎπΏππ-ππ΄π²π·π](https://t.me/OpusTechz)
β£βͺΌ ππΏπ³π°ππ΄π :- [πΌπ-ππΏπ³π°ππ΄π](https://t.me/MWUpdatez)
β£βͺΌ ππ π²π·π°π½π½π΄π»  :- [πΎπΏππ ππ΄π²π·π](https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA)
 
πΏπ»π΄π°ππ΄ ππ·π°ππ΄ π°π½π³ πππΏπΏπΎππ..//**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β πππ±ππ²ππΈπ±π΄ β", url=f"https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bff8d2c2ba43449adbc99.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π π³π΄πΏπ»πΎπ ππππΎππΈπ°π» π", url=f"https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA")
                ]
            ]
        ),
    )
