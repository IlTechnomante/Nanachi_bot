from random import choice
from glob import glob
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# from typing import TYPE_CHECKING, Any

from dotenv import load_dotenv
import os  # provides ways to access the Operating System and allows us to read the environment variables

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')

# b = (str("manga", "fumetto"))
a = "manga"


def start(update, context):
    update.message.reply_text("n-naaaah!")


def reply(update, context):
    testo = update.message.text.lower()

    if range("che fai", "come va") in testo:
        update.message.reply_text("ma fatti un po' gli affaracci tuoi! >:C")
    elif "ciao" in testo:
        update.message.reply_text("come andiamo?")
    elif a in testo:
        update.message.reply_text(
            "eccolo quà, c'è sia la versione in jap, che quello tradotto eng: https://new.madeinabyss.net/chapters/en_01_001.html#viewer buona lettura =^__^=")
    elif "scusa" in testo:
        update.message.reply_text("ok dai, scuse accettate =w=")
    elif "canta" in testo:
        update.message.reply_text("eh va bene.. ma solo in giapponese!")
        audio = choice(glob("Nanachi1/*.mp3"))
        update.message.reply_audio(open(audio, 'rb'))


    else:
        update.message.reply_text("ti..ti potresti allontanare un po'?")


updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))
print("nanachi ti vede ")
updater.start_polling()