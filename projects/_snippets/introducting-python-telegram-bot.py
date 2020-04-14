from telegram import Bot

# initializing the bot with API
bot = Bot("API KEY")

# getting the bot details
print(bot.get_me())