#plugin maked by @thanosceo for thanos pro kang with proper credits 
import asyncio

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd

from . import *


@borg.on(admin_cmd(outgoing=True, pattern="^Ilovu$"))
async def _(event):
    await event.edit("I LOVE U JAAN!")
    await asyncio.sleep(3)
    await event.edit(
        """
"   █\n" 
" ▒█░\n"
" ▄█▄\n"
"
" ▒█░░░\n"
" ▒█░░░\n"
" ▒█▄▄█\n"

" ▒█▀▀▀█\n"
" ▒█░░▒█\n"
" ▒█▄▄▄█\n" 

" ▒█░░▒█\n"
" ░▒█▒█░\n"
" ░░▀▄▀░\n"

" ▒█░▒█\n"
" ▒█░▒█\n"
" ░▀▄▄▀\n"
"""
    )


CmdHelp("ILOVEU").add_command("^Ilovu", None, "PROPOS YOUR crush").add()
