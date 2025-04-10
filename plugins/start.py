import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from info import Config, Txt


@Client.on_message(filters.private & filters.command('start'))
async def handle_start(bot:Client, message:Message):

    Btn = [
        [InlineKeyboardButton(text='💀 𝐇ᴇʟᴘ 💀', callback_data='help'), InlineKeyboardButton(text='🍑 𝐒ᴇʀᴠᴇʀ 𝐒ᴛᴀᴛs ☣️', callback_data='server')],
        [InlineKeyboardButton(text='💀 𝐔ᴘᴅᴀᴛᴇs ☠️', url='https://t.me/Honey_networks'), InlineKeyboardButton(text='⛔ 𝐀ʙᴏᴜᴛ ⛔', callback_data='about')],
        [InlineKeyboardButton(text='💀 𝐏ᴀᴘᴀ 💀', url='https://t.me/OgHoneyy')]
        ]

    await message.reply_text(text=Txt.START_MSG.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(Btn))


#Restart to cancell all process 
@Client.on_message(filters.private & filters.command("restart") & filters.user(Config.SUDO))
async def restart_bot(b, m):
    await m.reply_text("🏎️💨__𝐑ᴇꜱᴛᴀʀᴛɪɴɢ.....__")
    os.execl(sys.executable, sys.executable, *sys.argv)
