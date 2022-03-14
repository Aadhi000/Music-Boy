# Copyright (C) 2022 By #SmokerMusicX

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command, other_filters
from helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command(["rmd", "clear"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙰𝙻𝙻 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝙳 𝙵𝙸𝙻𝙴𝚉** ✅")
    else:
        await message.reply_text("🚫 **𝙽𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝙳 𝙵𝙸𝙻𝙴𝚉** 🚫")

        
@Client.on_message(command(["rmw", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("✅ **𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙰𝙻𝙻 𝚁𝙰𝚆 𝙵𝙸𝙻𝙴𝚉** ✅")
    else:
        await message.reply_text("🚫 **𝙽𝙾 𝚁𝙰𝚆 𝙵𝙸𝙻𝙴𝚉** 🚫")


@Client.on_message(command(["cleanup"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅ **𝙲𝙻𝙴𝙰𝙽𝙴𝙳** ✅")
    else:
        await message.reply_text("✅ **𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙲𝙻𝙴𝙰𝙽𝙴𝙳** ✅")
