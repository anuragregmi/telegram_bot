from .user import User
import telepot

class Message:
    """
    Telegram Message

    Attributes:
    `id`: id of the message.
    `chat_id`: id of the chat. It is where you send message or reply to.
    `chat_type`: Type of chat. It can be `group` or `private` for group chat or
        or private chat.
    `content_type`: Content type of the message. It can be 'text', 'photo',
        'document' etc.
    `date`: Sent date. Looks like a timestamp. Yet to figure out.
    `text`: Text message if message content_type is text.
    `sender`: User who sent the message. Refer to `User` docstring fot more details
        on User.
    """
    def __init__(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)
        self.id = str(message.get('id', None))
        self.chat_id = str(chat_id)
        self.chat_type = str(chat_type)
        self.content_type = str(content_type)
        self.date = str(message.get('date'))
        self.text = str(message.get('text'))
        self.sender = User(**message.get('from'))
