from telegram import Update, Bot
from telegram.ext import run_async
import telegram

from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot import dispatcher

import random
import time

@run_async
def flash(bot: Bot, update: Update):
    message = update.effective_message
    text = message.text[len('/flash '):]
    bot.sendChatAction(update.effective_chat.id, 'TYPING')
    r = random.randint(1, 10000)
    if len(text.split(" ")) > 1:
        return message.reply_text("`Cannot flash file!`")
    time.sleep(4)
    if r % 2 == 1:
        return message.reply_text(f"Successfully flashed {text}.zip!", telegram.ParseMode.MARKDOWN)
    elif r % 2 == 0:
        return message.reply_text(f"Flashing {text}.zip failed successfully!", telegram.ParseMode.MARKDOWN)

__help__ = """
Flash a file. Originally from NunoBot++.

Usage: /flash <file>
"""

__mod_name__ = "Flasher"
ud_handle = DisableAbleCommandHandler("flash", flash)
dispatcher.add_handler(ud_handle)