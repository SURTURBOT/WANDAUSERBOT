from userbot.cmdhelp import CmdHelp

from . import *


@borg.on(admin_cmd(outgoing=True, pattern="^Hi$"))
async def hi(event):
    giveVar = event.text
    rishabh = giveVar[4:5]
    if not rishabh:
        rishabh = "š„"
    await edit_or_reply(
        event,
        f"{rishabh}š«š«{rishabh}š«{rishabh}{rishabh}{rishabh}\n{rishabh}š«š«{rishabh}š«š«{rishabh}š«\n{rishabh}{rishabh}{rishabh}{rishabh}š«š«{rishabh}š«\n{rishabh}š«š«{rishabh}š«š«{rishabh}š«\n{rishabh}š«š«{rishabh}š«{rishabh}{rishabh}{rishabh}\nšššššššš",
    )


CmdHelp("Hii").add_command("^Hi", None, "Use and See").add()
