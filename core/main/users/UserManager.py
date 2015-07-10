from persistence.PersistenceExecutionError import PersistenceExecutionError
from persistence.PersistenceValidationError import PersistenceValidationError
from users.UserAuthenticationError import UserAuthenticationError
from users.UserExecutionError import UserExecutionError
from users.UserProfile import UserProfile
from users.UserValidationError import UserValidationError


class UserManager:
    _CREATION_FAIL_MESSAGE = 'User creation failed: '
    _DELETION_FAIL_MESSAGE = 'User deletion failed: '
    _ROLE_REMOVAL_FAIL_MESSAGE = 'Roles removal failed: '
    _AUTHENTICATION_FAIL_MESSAGE = 'User authentication failed: '
    _VALIDATION_FAIL_MESSAGE = 'User validation failed: '

    def __init__(self, data_persistence_manager, cloud_service_registry):
        self.__data_persistence_manager = data_persistence_manager
        self.__cloud_service_registry = cloud_service_registry

    def add_roles_to_user(self, username, roles):
        user = self.read_user(username)
        user.add_roles(roles)

        try:
            return self.__data_persistence_manager.update_element(username,
                                                                  user)
        except PersistenceValidationError as e:
            raise UserValidationError(str(e))
        except PersistenceExecutionError as e:
            raise UserExecutionError(str(e))

    def remove_roles_from_user(self, username, roles):
        user = self.read_user(username)
        user.remove_roles(roles)

        try:
            self.__data_persistence_manager.update_element(username, user)
        except PersistenceValidationError as e:
            raise UserValidationError(str(e))
        except PersistenceExecutionError as e:
            raise UserExecutionError(str(e))

    def read_user(self, username):
        try:
            return self.__data_persistence_manager.read_element(username)
        except PersistenceValidationError as e:
            raise UserValidationError(str(e))
        except PersistenceExecutionError as e:
            raise UserExecutionError(str(e))

    def change_user_password(self, username, password):
        user = self.read_user(username)
        user.set_unhashed_password(password)

        try:
            return self.__data_persistence_manager.update_element(username,
                                                                  user)
        except PersistenceValidationError as e:
            raise UserValidationError(str(e))
        except PersistenceExecutionError as e:
            raise UserExecutionError(str(e))

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
                    self._CREATION_FAIL_MESSAGE + str(e))

        raise UserValidationError(
            self._CREATION_FAIL_MESSAGE + "user already exists.")

    # TODO: implement soon
    def _user_is_owner(self, username):
        user = self.read_user(username)
        return False

    def delete_user(self, username):
        if self._user_is_owner(username):
            raise UserExecutionError(
                self._DELETION_FAIL_MESSAGE +
                "Can't delete a user that owns files."
            )

        try:
            return self.__data_persistence_manager.delete_element(username)
        except PersistenceValidationError as e:
            raise UserValidationError(str(e))
        except PersistenceExecutionError as e:
            raise UserExecutionError(
                self._DELETION_FAIL_MESSAGE + str(e))

    def get_all_users(self):
        try:
            return self.__data_persistence_manager.get_all_elements()
        except PersistenceValidationError as e:
            raise UserValidationError(str(e))
        except PersistenceExecutionError as e:
            raise UserExecutionError(
                self._ROLE_REMOVAL_FAIL_MESSAGE + str(e))

    def set_user_roles(self, username, roles):
        user = self.read_user(username)
        user.set_roles(roles)

        try:
            self.__data_persistence_manager.update_element(username, user)
        except PersistenceValidationError as e:
            raise UserValidationError(str(e))
        except PersistenceExecutionError as e:
            raise UserExecutionError(
                self._ROLE_REMOVAL_FAIL_MESSAGE + str(e))

    def verify_user_rights(self, username, password, role):
        user = self.read_user(username)
        if not user.validate_password(password):
            raise UserAuthenticationError(
                self._AUTHENTICATION_FAIL_MESSAGE + 'Incorrect password.')

        if not user.is_in_role(role):
            raise UserValidationError(
                self._VALIDATION_FAIL_MESSAGE +
                "The user doesn't have the rights to do this action.")
