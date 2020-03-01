from enum import Enum


class UserType(Enum):
    ANALYST = 1
    LEAD = 2


class User(object):

    def __init__(self, user_name, user_type):
        self.user_name = user_name
        self.user_type = user_type
