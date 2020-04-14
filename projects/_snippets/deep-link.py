from telegram.bot import Bot
from telegram.utils.helpers import create_deep_linked_url
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update
from telegram.ext.updater import Updater
import re

updater = Updater("API KEY", use_context=True)

def generate(update: Update, context: CallbackContext):
    """
    method to create a deep link and send it to the current user for sharing
    """

    # generating a sharable link with the payload
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.utils.helpers.html#telegram.utils.helpers.create_deep_linked_url
    url = create_deep_linked_url(context.bot.get_me().username, update.message.chat.username)
    update.message.reply_text(text="Share it with your friends: %s.\n Copy the link and share it with them" % url)
    pass


def start(update: Update, context: CallbackContext):
    """
    method to run on 
    """

    # extracting the payload with /start
    _ = re.findall(r"(?:/start )(.+)", update.message.text)

    # checking if it exists and sending message accordingly
    if len(_) > 0:
        update.message.reply_text(text="You have been refered by: %s" % _[0])
        pass
    else:
        update.message.reply_text(text="Hello, It seems you are new to this bot")
        pass

    update.message.reply_text(text="Use /generate to create your own referal")
    pass


updater.dispatcher.add_handler(CommandHandler("generate", generate))
updater.dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()