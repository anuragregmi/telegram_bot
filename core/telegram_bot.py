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
            if message.chat_type == 'group':
                self.handle_group_message(message)
            elif message.chat_type == 'private':
                self.handle_private_message(message)

    def handle_private_message(self, message):
        if message.sender.username in config.KNOWN_USERS:
            self.bot.sendMessage(
                message.chat_id,
                "I am working on private chat at the moment"
            )

    def handle_group_message(self, message):
        username = '@{}'.format(config.USERNAME)

        if username in message.text:
            print(message.sender.username, message.sender.id, message.text)
            if message.sender.username in config.KNOWN_USERS:
                reply_message= ""
                text = message.text.lower()
                for reply in config.REPLIES:
                    if reply in text:
                        reply_message += "{} ".format(config.REPLIES[reply])

                if reply_message.__len__() != 0:
                    self.bot.sendMessage(message.chat_id, reply_message)
            else:
                self.bot.sendMessage(message.chat_id, config.UNKNOWN_USER_REPLY)

    def run_bot(self):
        MessageLoop(
            self.bot,{
                'chat':self.handle_message,
            }
        ).run_as_thread()

        print("Listening . . .")

        while 1:
            time.sleep(10)
