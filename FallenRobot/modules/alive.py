import random

from pyrogram import __version__ as pyrover
from telegram import __version__ as telever
from telethon import Button
from telethon import __version__ as tlhver

from FallenRobot import OWNER_USERNAME, SUPPORT_CHAT, dispatcher
from FallenRobot import telethn as tbot
from FallenRobot.events import register

ANIMATION = [
    "https://telegra.ph/file/9d2fbe40731e96d0f7b25.mp4",
    "https://telegra.ph/file/9d2fbe40731e96d0f7b25.mp4",
]


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hello​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nI am{dispatcher.bot.first_name}**\n☆━━━━━━━━━━━━━━━━☆\n\n"
    TEXT += f"**Creator :** [Akhil 🇮🇳](tg://user?id={2102783671})** \n\n"
    TEXT += f"**Library Version:** `{telever}` \n\n"
    TEXT += f"**Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"**Pyrogram Version :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            Button.url("Help​", f"https://t.me/{dispatcher.bot.username}?start=help"),
        ]
    ]
    ran = random.choice(ANIMATION)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


__mod_name__ = "Alive"
