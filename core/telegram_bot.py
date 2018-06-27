import time
from config import config
from telepot import Bot

from telepot.loop import MessageLoop
from .message import Message

class TelegramBot:
    """
    Telegram Bot.

    Arrributes:
    `bot`: A telepot bot.

    Methods:
    `handle_message`: Handles a chat message
    `handle_private_message`: Handles private messages
    `handle_group_message`: Handles group messages

    Usage:

    # First of all create a telepot Bot.
    bot = telepot.Bot("TOKEN")

    # Then create a TelegramBot
    t_bot = TelegramBot(bot)

    # Then run telegram Bot
    t_bot.run_bot()

    Advanced:

    Override `handle_group_message` to handle group message your way and
    `handle_private_message` to handle private message your way
    """

    def __init__(self, bot):
        """
        Initializes TelegramBot

        :param bot: a telepot Bot instance
        :type bot: Bot
        """
        if isinstance(bot, Bot):
            self.bot = bot
        else:
            raise TypeError(
                "{} expected first argument to be a `Bot` object but \
                found `{}`".format(self.__class__.__name__,
                 bot.__class__.__name__)
            )

    def handle_message(self, msg):
        """
        Handle chat messages

        :param msg: Message dictionary
        :type msg: dict
        """
        message = Message(msg)
        if message.content_type == 'text':
            if message.chat_type == 'group':
                self.handle_group_message(message)
            elif message.chat_type == 'private':
                self.handle_private_message(message)

    def handle_private_message(self, message):
        """
        Handle private message

        :param message: Message object
        :type message: Message
        """
        if message.sender.username in config.KNOWN_USERS:
            self.bot.sendMessage(
                message.chat_id,
                "I am working on private chat at the moment"
            )

    def handle_group_message(self, message):
        """
        Handle group messages

        :param message: Message object
        :type message: Message
        """
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
        """
        Run the bot or start Listening
        """
        MessageLoop(
            self.bot,{
                'chat':self.handle_message,
            }
        ).run_as_thread()

        print("Listening . . .")

        while 1:
            time.sleep(10)
