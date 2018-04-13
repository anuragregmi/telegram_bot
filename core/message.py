from .user import User
import telepot

VALID_MESSAGE_ATTRS = ['id', 'text', 'date']

class Message:
    def __init__(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)
        for attr in VALID_MESSAGE_ATTRS:
            setattr(self, attr, message.get(attr, None))

        self.sender = User(**message.get('from'))
        self.chat_id = chat_id
        self.chat_type = chat_type
        self.content_type = content_type
