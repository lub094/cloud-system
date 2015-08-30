import hashlib


class UserProfile(object):

    def __init__(self, username='', password='', roles=[]):
        self.__username = username
        self.__password = self.__hash_password(password)
        self.__roles = roles

    def add_role(self, role):
        self.__roles.append(role)

    def add_roles(self, roles):
        self.__roles += roles

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
        hasher = hashlib.md5()
        hasher.update(password.encode('utf-8'))
        return hasher.hexdigest()

    def set_unhashed_password(self, password):
        self.__password = self.__hash_password(password)

    def is_in_role(self, role):
        return role in self.__roles

    def validate_password(self, unhashed_password):
        hashed_password = self.__hash_password(unhashed_password)
        return self.__password == hashed_password

    def remove_role(self, role):
        if role in self.__roles:
            self.__roles.remove(role)

    def remove_roles(self, roles):
        for role in roles:
            self.remove_role(role)

    def __str__(self):
        return self.__username

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
