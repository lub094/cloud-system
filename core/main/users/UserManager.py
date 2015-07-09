from persistence.PersistenceExecutionError import PersistenceExecutionError
from persistence.PersistenceValidationError import PersistenceValidationError
from users.UserAuthenticationError import UserAuthenticationError
from users.UserExecutionError import UserExecutionError
from users.UserProfile import UserProfile
from users.UserValidationError import UserValidationError

__author__ = 'Lubo'


class UserManager:
    CREATION_FAIL_MESSAGE = 'User creation failed: '
    DELETION_FAIL_MESSAGE = 'User deletion failed: '
    ROLE_REMOVAL_FAIL_MESSAGE = 'Roles removal failed: '
    AUTHENTICATION_FAIL_MESSAGE = 'User authentication failed: '
    VALIDATION_FAIL_MESSAGE = 'User validation failed: '

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

        try:
            return self.__data_persistence_manager.update_element(username,
                                                                  user)
        except PersistenceValidationError as e:
            raise UserValidationError(e.message)
        except PersistenceExecutionError as e:
            raise UserExecutionError(e.message)

    def remove_roles_from_user(self, username, roles):
        user = self.read_user(username)
        user.remove_roles(roles)

        try:
            self.__data_persistence_manager.update_element(username, user)
        except PersistenceValidationError as e:
            raise UserValidationError(e.message)
        except PersistenceExecutionError as e:
            raise UserExecutionError(e.message)

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
            return self.__data_persistence_manager.update_element(username,
                                                                  user)
        except PersistenceValidationError as e:
            raise UserValidationError(e.message)
        except PersistenceExecutionError as e:
            raise UserExecutionError(e.message)

    def create_user(self, username, password, roles):
        try:
            self.read_user(username)
        except UserValidationError:
            new_user = UserProfile(username)
            new_user.set_unhashed_password(password)
            new_user.set_roles(roles)

            try:
                return self.__data_persistence_manager.create_element(username,
                                                                      new_user)
            except (
                    PersistenceValidationError,
                    PersistenceExecutionError) as e:
                raise UserExecutionError(
                    self.CREATION_FAIL_MESSAGE + e.message)

            raise UserValidationError(
                self.CREATION_FAIL_MESSAGE + "user already exists.")

    def _user_is_owner(self, username):
        return False

    def delete_user(self, username):
        if self._user_is_owner(username):
            raise UserExecutionError(
                self.DELETION_FAIL_MESSAGE +
                "Can't delete a user that owns files."
            )

        try:
            return self.__data_persistence_manager.delete_element(username)
        except PersistenceValidationError as e:
            raise UserValidationError(e.message)
        except PersistenceExecutionError as e:
            raise UserExecutionError(
                self.DELETION_FAIL_MESSAGE + e.message)

    def get_all_users(self):
        try:
            return self.__data_persistence_manager.get_all_elements()
        except PersistenceValidationError as e:
            raise UserValidationError(e.message)
        except PersistenceExecutionError as e:
            raise UserExecutionError(
                self.ROLE_REMOVAL_FAIL_MESSAGE + e.message)

    def set_user_roles(self, username, roles):
        user = self.read_user(username)
        user.set_roles(roles)

        try:
            self.__data_persistence_manager.update_element(username, user)
        except PersistenceValidationError as e:
            raise UserValidationError(e.message)
        except PersistenceExecutionError as e:
            raise UserExecutionError(
                self.ROLE_REMOVAL_FAIL_MESSAGE + e.message)

    def verify_user_rights(self, username, password, role):
        user = self.read_user(username)
        user = UserProfile()
        if not user.validate_password(password):
            raise UserAuthenticationError(
                self.AUTHENTICATION_FAIL_MESSAGE + 'Incorrect password.')

        if not user.is_in_role(role):
            raise UserValidationError(
                self.VALIDATION_FAIL_MESSAGE +
                "The user doesn't have the rights to do this action.")
