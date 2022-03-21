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
        caption=f"""**𝚃𝙷𝙸𝚂 𝙸𝚂 𝙰𝙽 𝙰𝙳𝚅𝙰𝙽𝙲𝙴𝙳 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙼𝚄𝚂𝙸𝙲 𝙱𝙾𝚃 𝚁𝚄𝙽𝚂 𝙾𝙽 𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝚅𝙿𝚂 𝚆𝙸𝚃𝙷 𝙷𝙸𝙶𝙷 𝚀𝚄𝙰𝙻𝙸𝚃𝚈 𝙼𝚄𝚂𝙸𝙲 𝙰𝙽𝙳 𝚂𝚄𝙿𝙴𝚁 𝚂𝙿𝙴𝙴𝙳.𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽 𝚃𝙷𝙴𝙽 𝚂𝙴𝙰𝚁𝙲𝙷 𝚈𝙾𝚄𝚁 𝙵𝙰𝚅𝙾𝚁𝙸𝚃𝙴 𝚂𝙾𝙽𝙶𝚂 𝚆𝙸𝚃𝙷 𝙲𝙾𝙼𝙼𝙰𝙽𝙳...//

┣⪼ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 :- [𝙾𝙿𝚄𝚂-𝚃𝙴𝙲𝙷𝚉](https://t.me/OpusTechz)
┣⪼ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 :- [𝙼𝚆-𝚄𝙿𝙳𝙰𝚃𝙴𝚉](https://t.me/MWUpdatez)
┣⪼ 𝚈𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻  :- [𝙾𝙿𝚄𝚂 𝚃𝙴𝙲𝙷𝚉](https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA)
 
𝙿𝙻𝙴𝙰𝚂𝙴 𝚂𝙷𝙰𝚁𝙴 𝙰𝙽𝙳 𝚂𝚄𝙿𝙿𝙾𝚁𝚃..//**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴 ✅", url=f"https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA")
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
                        "💌 𝙳𝙴𝙿𝙻𝙾𝚈 𝚃𝚄𝚃𝙾𝚁𝙸𝙰𝙻 💌", url=f"https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA")
                ]
            ]
        ),
    )
