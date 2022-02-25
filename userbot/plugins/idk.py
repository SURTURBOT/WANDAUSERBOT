# this plugin maked by @thanosceo for thanos pro kang with credits 
#thanos pro
import asyncio
from userbot import *
from THANOSBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from userbot import ALIVE_NAME
#thanospro
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "THANOSBOT"


@borg.on(admin_cmd(outgoing=True, pattern="^idk$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 17)
    await event.edit("⚡")
    animation_chars = [
        "I DON'T",
        "KNOW",
        f"I DON'T KNOW",    
    ]
    for i in animation_ttl:  # By @thanosceo for thanos bot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 



@borg.on(admin_cmd(outgoing=True, pattern="^Idc$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 17)
    await event.edit("⚡")
    animation_chars = [
        "I don't care",
        "I don't care",
        f"I don't care",    
    ]
    for i in animation_ttl:  # By @thanosceo for thanos bot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 



@borg.on(admin_cmd(outgoing=True, pattern="^Kn$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 17)
    await event.edit("⚡")
    animation_chars = [
        "Kuch",
        "Nhi",
        f"kuch nhi",    
    ]
    for i in animation_ttl:  # By @thanosceo for thanos bot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 


@borg.on(admin_cmd(outgoing=True, pattern="^Fu$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 17)
    await event.edit("⚡")
    animation_chars = [
        "Fuck",
        "Fuck u",
        f"fuck you",    
    ]
    for i in animation_ttl:  # By @thanosceo for thanos bot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 



from userbot.cmdhelp import CmdHelp

CmdHelp("SHORT1").add_command("^Idk", None, "Use and see").add_command( 
    "^Idc", None, "Use and see  girls"
).add_command("^Kn", None, "Use and see").add_command(
    "^Fu", None, "Use and see"
).add()
