from userbot.cmdhelp import CmdHelp
from userbot.utils import *


@bot.on(admin_cmd(pattern=r"shouts", outgoing=True))
@bot.on(sudo_cmd(pattern=r"shouts", allow_sudo=True))
async def shouts(args):
    if args.fwd_from:
        return
    else:
        msg = "```"
        messagestr = args.text
        messagestr = messagestr[7:]
        text = " ".join(messagestr)
        result = []
        result.append(" ".join([s for s in text]))
        for pos, symbol in enumerate(text[1:]):
            result.append(symbol + " " + "  " * pos + symbol)
        result = list("\n".join(result))
        result[0] = text[0]
        result = "".join(result)
        msg = "\n" + result
        await args.edit("`" + msg + "`")


CmdHelp("shouts").add_command(
    "shouts", "<text>", "Shouts your message in meme way.", ".shouts Thanos"
).add()
