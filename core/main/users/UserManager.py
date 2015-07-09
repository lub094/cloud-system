from persistence.PersistenceExecutionError import PersistenceExecutionError
from persistence.PersistenceValidationError import PersistenceValidationError
from users.UserExecutionError import UserExecutionError
from users.UserProfile import UserProfile
from users.UserValidationError import UserValidationError

__author__ = 'Lubo'


class UserManager:
    CREATION_FAIL_MESSAGE = 'User creation failed: '

    def __init__(self):
        self.__binaries_location = ""
        self.__cloud_service_registry = None
        self.__file_persistence_manager = None
        self.__data_persistence_manager = None

    def get_binary(self):
        pass

    def get_all_binaries(self):
        pass

    def used_by_a_task(self):
        pass

    def delete_binary(self):
        pass

    def deploy_binary(self):
        pass

    def create_binary(self):
        pass

    def get_binary_file(self):
        pass

    def get_repository_location(self):
        pass

    def add_roles_to_user(self, username, roles):
        user = self.read_user(username)
        user.add_roles(roles)

        return self.__data_persistence_manager.update_element(username, user)

    def read_user(self, username):
        try:
            return self.__data_persistence_manager.read_element(username)
        except PersistenceValidationError as e:
            raise UserValidationError(e.message())
        except PersistenceExecutionError as e:
            raise UserExecutionError(e.message())

    def change_user_password(self, username, password):
        user = self.read_user(username)
        user.set_unhashed_password(password)

        try:
            return self.__data_persistence_manager.update_element(username, user)
        except PersistenceValidationError as e:
            raise UserValidationError(e.message)
        except PersistenceExecutionError as e:
            raise UserExecutionError(e.message)

    def create_user(self, username, password, roles):
        try:
            self.read_user(username)
        except UserValidationError as e:
            new_user = UserProfile(username)
            new_user.set_unhashed_password()

        raise UserValidationError(self.CREATION_FAIL_MESSAGE + "user already exists.")