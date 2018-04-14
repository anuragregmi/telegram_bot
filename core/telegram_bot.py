import time
from config import config

from telepot.loop import MessageLoop
from .message import Message

class TelegramBot:
    def __init__(self, bot):
        self.bot = bot

    def handle_message(self, msg):
        message = Message(msg)

        if message.content_type == 'text':
            if message.sender.username in config.KNOWN_USERS:
                self.bot.sendMessage(
                    message.chat_id,
                    "{} bhai maile chinxu ni timilai.".format(
                    message.sender.first_name)
                )
            else:
                self.bot.sendMessage(
                    message.chat_id, "Maile chinena ni tapailai.")

    def run_bot(self):
        MessageLoop(
            self.bot,{
                'chat':self.handle_message,
            }
        ).run_as_thread()

        print("Listening . . .")

        while 1:
            time.sleep(10)
