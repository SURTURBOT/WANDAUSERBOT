import asyncio

from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="test ?(.*)"))
@bot.on(sudo_cmd(pattern="test ?(.*)", allow_sudo=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):

        await edit_or_reply(event, "`Testing THANOSBOT`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing THANOSBOT.`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing THANOSBOT..`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing THANOSBOT...`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing THANOSBOT....`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing THANOSBOT.....`")
        await asyncio.sleep(2)
        await edit_or_reply(event, "__Testing Successful__")
        await asyncio.sleep(2)
        await edit_or_reply(event, "`Generating Output`\nPlease wait")
        await asyncio.sleep(2)
        await edit_or_reply(event, "__Output Generated Successfully__")
        await asyncio.sleep(2)
        await edit_or_reply(event, "**SAVING OUTPUT TO THANOSBOT LOCAL DATABASE**")
        await asyncio.sleep(3.5)
        await edit_or_reply(
            event,
            "Your [THANOSBOT](https:/t.me/thanosbot_chats) is working Fine...\n       Join @thanosbot_chats For Any Help......",
        )


CmdHelp("test").add_command(
    "test", None, "Test wether your bot is running or not."
).add()
