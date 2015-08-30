import sys
from core.main.users.user_validation_error import UserValidationError
sys.path.append(
    'X:\OneDrive\Programming\Code\Python\Projects\CloudSystem\cloud-system')

from core.main.persistence.persistence_validation_error import \
    PersistenceValidationError
import unittest
from core.main.users.user_manager import UserManager
from core.main.users.user_role import UserRole
from core.main.users.user_profile import UserProfile


class DataPersistenceManagerStub:

    def __init__(self):
        self.__elements = {}

    def update_element(self, key, element):
        if key in self.__elements:
            self.__elements[key] = element
        else:
            raise PersistenceValidationError('Element does not exist')

    def read_element(self, key):
        try:
            return self.__elements[key]
        except:
            raise UserValidationError('Element does not exist')

    def create_element(self, key, element):
        self.__elements[key] = element

    def delete_element(self, key):
        del self.__elements[key]

    def get_all_elements(self):
        return self.__elements.values()


class TestUserManager(unittest.TestCase):

    def setUp(self):
        self.username = 'lubo'
        self.password = 'pwd'
        self.roles = [UserRole.ADMINISTRATOR]
        self.user_manager = UserManager(DataPersistenceManagerStub())
        self.user_manager.create_user(self.username, self.password, self.roles)

    def test_read_user(self):
        user = UserProfile(self.username, self.password, self.roles)

        self.assertEqual(self.user_manager.read_user('lubo'), user)

    def test_add_roles_to_user(self):
        role = UserRole.BASIC
        self.user_manager.add_roles_to_user(self.username, [role])

        self.assertTrue(
            role in self.user_manager.read_user(self.username).get_roles())

    def test_remove_roles_from_user(self):
        roles = [UserRole.BASIC]
        self.user_manager.add_roles_to_user(self.username, roles)
        self.user_manager.remove_roles_from_user(self.username, roles)

        for role in roles:
            self.assertTrue(role not in self.user_manager.
                            read_user(self.username).get_roles())

    def test_change_user_password(self):
        new_password = 'pass'
        self.user_manager.change_user_password(self.username, new_password)
        user = self.user_manager.read_user(self.username)

        self.assertTrue(user.validate_password(new_password))

    def test_delete_user(self):
        self.user_manager.delete_user(self.username)

        with self.assertRaises(UserValidationError):
            self.user_manager.read_user(self.username)

    def test_get_all_users(self):
        username = 'temp'
        password = 'pass'
        roles = []
        user1 = UserProfile(username, password, roles)
        user2 = UserProfile(self.username, self.password, self.roles)
        self.user_manager.create_user(username, password, roles)

        self.assertIn(user1, self.user_manager.get_all_users())
        self.assertIn(user2, self.user_manager.get_all_users())

    def test_set_user_roles(self):
        roles = [UserRole.BASIC]
        self.user_manager.set_user_roles(self.username, roles)

        self.assertIn(
            UserRole.BASIC, self.user_manager.read_user(self.username).
            get_roles())
        self.assertNotIn(
            UserRole.ADMINISTRATOR, self.user_manager.read_user(self.username).
            get_roles())

    def test_verify_user_rights_success(self):
        self.user_manager.verify_user_rights(
            self.username, self.password, UserRole.ADMINISTRATOR)

    def test_verify_user_rights_fail(self):
        self.user_manager.set_user_roles(self.username, [])

        with self.assertRaises(UserValidationError):
            self.user_manager.verify_user_rights(
                self.username, self.password, UserRole.BASIC)

unittest.main()
