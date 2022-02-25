import asyncio

from userbot import ALIVE_NAME
from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd

from . import *

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "THANOSBOT User"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"

import asyncio
from userbot import *
from REBELBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "REBEL"


@borg.on(admin_cmd(outgoing=True, pattern="^Pm$"))
@borg.on(sudo_cmd(pattern="^Pm$", allow_sudo=True))
async def bluedevilpm(pm):
    if hello.fwd_from:
        return
    await pm.get_chat()
    good = await eor(Pm, "**(❛ pm ❜!**")
    if PM = f"ＰΞＲＳ♢ＮΛＬ ＭΞＳＳΛＧΞ ＫΛＲ♢\n"
       await good.delete()
 
    for i in animation_ttl:  # By @mafiarishabh for thanos bot

        await asyncio.sleep(animation_interval)
        await event.edit(
            animation_chars[i % 17], link_preview=True
        ) 


HELL_PIC = "https://te.legra.ph/file/b86eff074051b0b2d4513.jpg"
K_PIC = "https://te.legra.ph/file/a679e3d061ac6b349cd60.jpg"
L_PIC = "https://te.legra.ph/file/96c2b61d6361f112ceac5.jpg"
M_PIC = "https://te.legra.ph/file/4d0c641e085f7ed15dfec.jpg"


@borg.on(admin_cmd(outgoing=True, pattern="^Hell$"))
@borg.on(sudo_cmd(pattern="^Hell$", allow_sudo=True))
async def bluedevilhello(hell):
    if hello.fwd_from:
        return
    await hello.get_chat()
    good = await eor(hello, "**(❛ Hi ❜!**")
    if HELL_PIC:
        HELLO = f"╔┓┏╦━╦┓╔┓╔━━╗\n"
        HELLO += f"║┗┛║┗╣┃║┃║X X ║\n"
        HELLO += f"║┏┓║┏╣┗╣┗╣╰╯║\n"
        HELLO += f"╚┛┗╩━╩━╩━╩━━╝\n"
        on = await borg.send_file(hello.chat_id, file=HELL_PIC, caption=HELLO)
        await asyncio.sleep(3)
        ok = await borg.edit_message(hello.chat_id, on, file=K_PIC)
        await asyncio.sleep(3)
        ok1 = await borg.edit_message(hello.chat_id, on, file=L_PIC)
        await asyncio.sleep(3)
        ok2 = await borg.edit_message(hello.chat_id, ok1, file=M_PIC)
        await asyncio.sleep(5)
        ok3 = await borg.edit_message(hello.chat_id, ok2, file=L_PIC)
        await asyncio.sleep(5)
        ok4 = await borg.edit_message(hello.chat_id, ok3, file=K_PIC)
        await asyncio.sleep(5)
        ok5 = await borg.edit_message(hello.chat_id, ok4, file=HELL_PIC)
        await good.delete()




CmdHelp("arts").add_command("elove", None, "Use and see").add_command(
    "monster", None, "Use and see"
).add_command("pig", None, "Use and see").add_command(
    "gun", None, "Use and see"
).add_command(
    "dog", None, "Use and see"
).add_command(
    "^Hello", None, "Use and see"
).add_command(
    "hmf", None, "Use and see"
).add_command(
    "couple", None, "Use and see"
).add_command(
    "sup", None, "Use and see"
).add_command(
    "india", None, "Use and see"
).add_command(
    "wc", None, "Use and see"
).add_command(
    "snk", None, "Use and see"
).add_command(
    "bye", None, "Use and see"
).add_command(
    "shitos", None, "Use and see"
).add_command(
    "dislike", None, "Use and see"
).add_command(
    "car", "<text>", "send your text with carry art"
).add_command(
    "ded", "<text>", "Hang yourself"
).add_command(
    "sthink", "<text>", "Send your text in thinking art"
).add_command(
    "sfrog", "<text>", "Send your text in frog art"
).add_command(
    "sdead", "<text>", "Send your text in dear frog art"
).add_command(
    "strump", "<text>", "Send your text in trump art"
).add_command(
    "china", "<text>", "Send your text in china art"
).add_command(
    "sshit", None, 'Send a art in "Ahh shit. Here we go again"'
).add()
