
VALID_USER_ATTRS = ['id', 'is_bot', 'first_name', 'username']

class User:
    def __init__(self, **kwargs):
        for attr in VALID_USER_ATTRS:
            setattr(self, attr, kwargs.get(attr, None))
