import asyncio
import datetime
import os

from .. import ALIVE_NAME
from ..cmdhelp import CmdHelp
from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import *


@bot.on(admin_cmd(pattern="ping$", outgoing=True))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    "To check ping"
    type = event.pattern_match.group(1)
    start = datetime.now()
    if type == " -a":
        THANOSBOTevent = await eor(event, "`!....`")
        await asyncio.sleep(0.3)
        await THANOSBOTevent.edit("`..!..`")
        await asyncio.sleep(0.3)
        await THANOSBOTevent.edit("`....!`")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.6) / 3, 3)
        await THANOSBOTevent.edit(f"**👨‍💻 Average Pong!**\n➥ {ms} ms")
    else:
        sweetie = (
            gvarstatus("PING_PIC")
            or "https://telegra.ph/file/bdf457aee34ed8791c150.jpg"
        )
        THANOSBOTevent = await eor(event, "<b><i>⚡ **Pong!** ⚡</b></i>", "html")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await THANOSBOTevent.delete()
        await event.client.send_file(
            event.chat_id,
            sweetie,
            caption=f"<b><i>👨‍💻 Pong </b></i>\n\n   🚩 {ms} <b><i>ms\n   Bot : {hmention}</b></i>",
            parse_mode="html",
        )
