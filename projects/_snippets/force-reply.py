from telegram.forcereply import ForceReply
from telegram.ext.filters import Filters
from telegram.ext.updater import Updater
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update

updater = Updater("API KEY", use_context=True)

def echo(update: Update, context: CallbackContext):
    # sending the force reply to the user
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.forcereply.html
    update.message.reply_text(reply_markup=ForceReply(selective=True), text="Reply to this message")
    pass

updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()