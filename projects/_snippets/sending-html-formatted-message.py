from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot
from telegram.parsemode import ParseMode

updater = Updater("API KEY",
                  use_context=True)

dispatcher: Dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    """
    the callback for handling start command
    """
    bot: Bot = context.bot

    # Added HTML Parser to the existing command handler
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.parsemode.html#telegram.ParseMode.HTML
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        "Hello User, You have used <b>start</b> command. Search about developer on google, <a href='https://www.google.com/search?q=tbhaxor'>@tbhaxor</a>",
        parse_mode=ParseMode.HTML,
    )


dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()