VALID_USER_ATTRS = ['id', 'is_bot', 'first_name', 'username']

class User:
    """
    A telegram user.

    Attributes:
    `id`: user id,
    `is_bot`: Boolean. True if user is bot.
    `first_name`: First Name of the user.
    `username`: username of the user.
    """
    def __init__(self, **kwargs):
        for attr in VALID_USER_ATTRS:
            setattr(self, attr, kwargs.get(attr, None))
