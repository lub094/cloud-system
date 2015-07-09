import hashlib
import uuid


class UserProfile:
    def __init__(self, username="", password="", roles=[]):
        self.__username = username
        self.__password = password
        self.__roles = roles

    def add_role(self, role):
        self.__roles.append(role)

    def add_roles(self, roles):
        self.__roles += roles

    # def clone(self): pass

    def get_password(self):
        return self.__password

    def get_username(self):
        return self.__username

    def get_roles(self):
        return self.__roles

    def set_roles(self, roles):
        self.__roles = roles

    @staticmethod
    def __hash_password(password):
        salt = uuid.uuid4().hex
        return hashlib.sha512(
            password.encode("utf-8") + salt.encode("utf-8")).hexdigest()

    def set_unhashed_password(self, password):
        self.__password = self.__hash_password(password)

    def is_in_role(self, role):
        return role in self.__roles

    def validate_password(self, unhashed_password):
        hashed_password = self.__hash_password(unhashed_password)
        return self.__password == hashed_password

    def __str__(self):
        return self.__username
