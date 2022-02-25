# this plugin maked by @thanosceo for thanos pro kang whith credits 
#thanos pro
import asyncio
from userbot import *
from THANOSBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from userbot import ALIVE_NAME
#thanospro
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "THANOSBOT"


@borg.on(admin_cmd(outgoing=True, pattern="^Mcb$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 17)
    await event.edit("⚡")
    animation_chars = [
        "SUNO",
        "TUM MADARCHOD HO 🤣🤣🤣 TERE MAA MAIN NE HI CHODA HAI",
        f"SUNO TUM MADARCHOD HO 🤣🤣🤣 TERE MAA MAIN NE HI CHODA HAI",    
    ]
    for i in animation_ttl:  # By @thanosceo for thanos bot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 



@borg.on(admin_cmd(outgoing=True, pattern="^Mc$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 17)
    await event.edit("⚡")
    animation_chars = [
        "SUNO",
        "TU MADARCHOD HAI🤣🤣🤣 TERE MAA MAIN NE HI CHODA HAI",
        f"SUNO PAGAL GIRL TU MADARCHOD HAI 🤣🤣🤣 TERE MAA MAIN NE HI CHODA HAI",    
    ]
    for i in animation_ttl:  # By @thanosceo for thanos bot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 



from userbot.cmdhelp import CmdHelp

CmdHelp("AGALI").add_command("^Mcb", None, "Use this plugin to boy and see").add_command( 
    "^Mc", None, "Use and see  girls"
).add_command("pig", None, "Use and see").add_command(
