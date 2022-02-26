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
"______$¦$¦$¦ ____ $¦$¦$¦$\n"
"____$¦$_____$$__$$_____$¦$\n"
"___$¦$________$$________$¦$\n"
"__ $¦$ I    LOVE   U    $¦$\n"
"___$¦$❤______________💙$¦$\n"
"_(¯`.´¯)$¦$____🤍_____$¦$(¯`.´¯)\n"
"(¯≻ ✦ ≺¯)$¦$_______$¦$(¯≻ ✦ ≺¯)\n"
"_(_.^._)____$¦$🤍 $¦$____ (_.^._)\n"
"✨✨_(¯`.´¯) __$¦$__ (¯`.´¯)\n"
"✨_ (¯≻ ✦ ≺¯) _ $_ (¯≻ ✦ ≺¯)\n"
"✨✨_(_.^._) (¯`.´¯)_(_.^._)\n"
"__________(¯≻ ✦ ≺¯)\n"
"✨✨_(¯`.´¯) (_.^._) (¯`.´¯)\n"
"___ (¯≻ ✦ ≺¯) ____(¯≻ ✦ ≺¯)\n"
"_____(_.^._) ______ (_.^._)\n"

"""
    )


CmdHelp("ILOVEU").add_command("^Iloveu", None, "PROPOS YOUR crush").add()
