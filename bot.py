from config import config
from telepot import Bot
from core import TerminalBot

bot  = TerminalBot(Bot(config.TOKEN))
bot.run_bot()
