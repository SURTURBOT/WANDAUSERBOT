from . import *


@bot.on(admin_cmd(pattern="sp"))
async def oho(event):
    if not event.is_reply:
        return await event.edit("Reply to a self distructing pic !.!.!")
    k = await event.get_reply_message()
    pic = await k.download_media()
    await bot.send_file(
        event.chat_id,
        pic,
        caption=f"""
  OwO!! LoL, Destruction Mode Pic Destroyed sed🤣🤣🤣!!
  Pic captured By THANOSBOT
😎😎
  """,
    )
    await event.delete()


CmdHelp("secretpic").add_command(
    "sp", "This Command Can Capture The Self Destruction Picture"
).add_info("Capture 🤫 Pic.").add_warning("✅ Harmless Module.").add()
