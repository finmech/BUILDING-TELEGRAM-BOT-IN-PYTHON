from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot

# initializing an updator
# documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.updater.html#telegram.ext.Updater
updater = Updater("API KEY",
                  use_context=True)

# getting the dispatcher required to handle the command /start and send message back to the user
# documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.dispatcher.html#telegram.ext.Dispatcher
dispatcher: Dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    """
    the callback for handling start command
    """
    # getting the bot from context
    # documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html#telegram-bot
    bot: Bot = context.bot

    # sending message to the chat from where it has received the message
    # documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html#telegram.Bot.send_message
    bot.send_message(chat_id=update.effective_chat.id,
                     text="You have just entered start command")


# register a handler (here command handler)
# documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.dispatcher.html#telegram.ext.Dispatcher.add_handler
dispatcher.add_handler(
    # it can accept all the telegram.ext.Handler, CommandHandler inherits Handler class
    # documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.commandhandler.html#telegram-ext-commandhandler
    CommandHandler("start", start))

# starting polling updates from Telegram
# documentation: https://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.updater.html#telegram.ext.Updater.start_polling
updater.start_polling()