from flask_login import UserMixin

from mysql_service import *


class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data):
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(user_id)
        pass
