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
______$¦$¦$¦ ____ $¦$¦$¦$
____$¦$_____$$__$$_____$¦$
___$¦$________$$________$¦$
__ $¦$ I    LOVE   U    $¦$
___$¦$❤______________💙$¦$
_(¯`.´¯)$¦$____🤍_____$¦$(¯`.´¯)
(¯≻ ✦ ≺¯)$¦$_______$¦$(¯≻ ✦ ≺¯)
_(_.^._)____$¦$🤍 $¦$____ (_.^._)
✨✨_(¯`.´¯) __$¦$__ (¯`.´¯)
✨_ (¯≻ ✦ ≺¯) _ $_ (¯≻ ✦ ≺¯)
✨✨_(_.^._) (¯`.´¯)_(_.^._)
__________(¯≻ ✦ ≺¯)
✨✨_(¯`.´¯) (_.^._) (¯`.´¯)
___ (¯≻ ✦ ≺¯) ____(¯≻ ✦ ≺¯)
_____(_.^._) ______ (_.^._)

"""
    )


CmdHelp("ILOVEU").add_command("^Iloveu", None, "PROPOS YOUR crush").add()
