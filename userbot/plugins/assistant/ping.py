import os

from telethon import Button, events

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

THANOSBOT_IMG = os.environ.get(
    "BOT_PING_PIC", "https://telegra.ph/file/c8fe5de96a7968636edc4.mp4"
)
ms = 4
ALIVE = Config.ALIVE_NAME

THANOS = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   💞 {ms}\n   💞 ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("💔THANOS-PRO💔", "https://t.me/THANOSBOT_CHATS")]]
    await tgbot.send_file(event.chat_id, THANOSBOT_IMG, caption=THANOS, buttons=GOOD)
