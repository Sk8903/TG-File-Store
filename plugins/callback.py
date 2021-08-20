import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from .commands import start, BATCH
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *

@Client.on_callback_query(filters.regex('^help$'))
async def help_cb(c, m):
    await m.answer()

    # help text
    help_text = """** உங்களுக்கு உதவி தேவையா ??**

நீங்கள் ஒன்றும் செய்யவேண்டாம் 


**எங்களுடைய சேனலில் கிடைக்கும் அப்டேட்ஸ் ஐ மட்டும் நீங்கள் பயன்படுத்தவும்**

★ நீங்கள் தேவை இல்லாமல் என்னை பயன்படுத்தினால் உங்களுக்கு கடுமையான தண்டனை கிடைக்கும்

**நன்றி 🙏**

★ """

    # creating buttons
    buttons = [
        [
            InlineKeyboardButton('Back To Home', callback_data='back to home'),
            InlineKeyboardButton('Current Version', callback_data='current version')
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]

    # editing as help message
    await m.message.edit(
        text=help_text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex('^close$'))
async def close_cb(c, m):
    await m.message.delete()
    await m.message.reply_to_message.delete()


@Client.on_callback_query(filters.regex('^currentversion$'))
async def about_cb(c, m):
    await m.answer()
    owner = await c.get_users(int(OWNER_ID))
    bot = await c.get_me()

    # about text
    about_text = f"""--**Current Version 🎗️**--

Current Version : 1:0
    
Next Version : 1:1

Old Version : 0:0 

What's New : New Ui(1:0)

Main Channel: [Sk Tv](https://t.me/Sk_Tv_Official)

Updates Channel: [Sk Tamil Serial Bots](https://t.me/Sk_Tamil_Serial_Bots)

Movies Channel : [Sk Tamil Movies](https://t.me/Sk_Tamil_Movies)
"""

    # creating buttons
    buttons = [
        [
            InlineKeyboardButton('Home ', callback_data='home'),
            InlineKeyboardButton('Help ', callback_data='help')
        ],
        [
            InlineKeyboardButton('Close ', callback_data='close')
        ]
    ]

    # editing message
    await m.message.edit(
        text=about_text,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex('^home$'))
async def home_cb(c, m):
    await m.answer()
    await start(c, m, cb=True)


@Client.on_callback_query(filters.regex('^done$'))
async def done_cb(c, m):
    BATCH.remove(m.from_user.id)
    c.cancel_listener(m.from_user.id)
    await m.message.delete()


@Client.on_callback_query(filters.regex('^delete'))
async def delete_cb(c, m):
    await m.answer()
    cmd, msg_id = m.data.split("+")
    chat_id = m.from_user.id if not DB_CHANNEL_ID else int(DB_CHANNEL_ID)
    message = await c.get_messages(chat_id, int(msg_id))
    await message.delete()
    await m.message.edit("Deleted files successfully 👨‍✈️")
