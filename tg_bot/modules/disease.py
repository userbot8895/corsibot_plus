import time
import random

from telegram import Message, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown

import tg_bot.modules.sql.disease_sql as sql
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

@run_async
def infect(bot: Bot, update: Update):
    repl = update.effective_message.reply_to_message
    if repl:
        repl_sender = repl.from_user
        if repl_sender.id == update.effective_message.from_user.id:
            update.effective_message.reply_text("Decided to end your life? I won't let you.")
            return
        #if f"[{repl_sender.first_name}](tg://user?id={repl_sender.id})" in read:
            #update.effective_message.reply_text(f"{replymsg.sender.first_name} was already infected by you or someone you merged patients with!")
            #return
        sql.infect(1337, f"[{repl_sender.first_name}](tg://user?id={repl_sender.id})")
        f.close()
        update.effective_message.reply_text(f"{repl_sender.first_name}, you are now infected with the {VIRUS}!")
    else:
        update.effective_message.reply_text("I don't know whom to infect!")

"""
async def share(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		await event.client.send_file(
			event.chat_id,
			"patients.txt",
			caption=f"This is a list of patients infected with the {VIRUS}.\
			\nReply with .infmerge to add {VIRUS}'s patients to your own virus' patient list."
        )
		await event.delete()
		
@register(outgoing=True, pattern=r"^.infmerge")
async def infmerge(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		replymsg = await event.get_reply_message()
		if replymsg:
			if replymsg.media:
				await event.edit("`Downloading file...`")

				downloaded_file_name = await bot.download_media(
					replymsg,
					"deldog_temp",
					progress_callback=progress
				)
				their_list = None
				with open(downloaded_file_name, "r", encoding="utf-8") as fd:
					their_list = fd.readlines()
				os.remove(downloaded_file_name)

				await event.edit("`Reading list...`")
				open('patients.txt', 'a').close()
				with open ("patients.txt", "r", encoding="utf-8") as rf:
					ours=rf.read()
				await event.edit("`Merging...`")
				pats = 0;
				with open ("patients.txt", "a", encoding="utf-8") as app:
					for pat in their_list:
						await event.respond(pat)
						if not pat in ours:
							app.write(pat)
							pats = pats + 1
				if pats != 0:
					await event.edit(f"The {VIRUS} just infected {pats} more patients from {replymsg.sender.first_name}'s list!")
				else:
					await event.edit(f"Everyone who was infected by {replymsg.sender.first_name} were already in the list!")
			else:
				await event.edit("Reply to a message containing patients.txt!")
		else:
			await event.edit("I don't know whom to merge lists with!")

@register(outgoing=True, pattern=r"^.infstats")
async def infected(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		rf=open("patients.txt", "r", encoding="utf-8")
		read=rf.read()
		rf.close()
		reply = f"List of people infected with the {VIRUS}:\n{read}"
		await event.edit(reply[0:4090])
"""

__help__ = """
 You've all heard of the COVID-19 pandemic.
 This is a sort of Telegram pandemic. TGVID-xx.

 This is a partial port of disease from HUB++. I'm releasing this as one last feature update, but I'm unsure if this works well, which is why I'm releasing this to a separate branch."""

__mod_name__ = "Disease"

INFECT_HANDLER = DisableAbleCommandHandler("infect", infect, filters=Filters.group)
dispatcher.add_handler(INFECT_HANDLER)
