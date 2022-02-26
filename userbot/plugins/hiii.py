from userbot.cmdhelp import CmdHelp

from . import *


@borg.on(admin_cmd(outgoing=True, pattern="^Hi$"))
async def hi(event):
    giveVar = event.text
    rishabh = giveVar[4:5]
    if not rishabh:
        rishabh = "💥"
    await edit_or_reply(
        event,
        f"{rishabh}💫💫{rishabh}💫{rishabh}{rishabh}{rishabh}\n{rishabh}💫💫{rishabh}💫💫{rishabh}💫\n{rishabh}{rishabh}{rishabh}{rishabh}💫💫{rishabh}💫\n{rishabh}💫💫{rishabh}💫💫{rishabh}💫\n{rishabh}💫💫{rishabh}💫{rishabh}{rishabh}{rishabh}\n💞💞💞💞💞💞💞💞",
    )


CmdHelp("Hii").add_command("^Hi", None, "Use and See").add()
