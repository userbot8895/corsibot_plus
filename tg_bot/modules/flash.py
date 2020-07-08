from telegram import Update, Bot
from telegram.ext import run_async

from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot import dispatcher

@run_async
def flash(bot: Bot, update: Update):
    message = update.effective_message
    text = message.text[len('/flash '):]
    r = random.randint(1, 10000)
    if len(text.split(" ")) > 1:
        return message.reply_text("`Cannot flash file!`")
    time.sleep(4)
    if r % 2 == 1:
        return message.reply_text(f"`Successfully flashed` {text}.zip`!`")
    elif r % 2 == 0:
        return message.reply_text(f"`Flashing` {text}.zip `failed successfully!`")

__help__ = """
Flash a file. Originally from nunobot++.

Usage: /flash <file>
"""

__mod_name__ = "Flasher"

ud_handle = DisableAbleCommandHandler("flash", ud)

dispatcher.add_handler(ud_handle)