from config import config
from telepot import Bot
from core import TelegramBot

bot  = TelegramBot(Bot(config.TOKEN))

if __name__ == '__main__':
    bot.run_bot()
