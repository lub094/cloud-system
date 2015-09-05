import unittest
from core.main.users.user_validation_error import UserValidationError
from core.main.persistence.ram_data_persistence_manager import \
    RamDataPersistenceManager
from core.main.users.user_manager import UserManager
from core.main.users.user_role import UserRole
from core.main.users.user_profile import UserProfile


class TestUserManager(unittest.TestCase):

    def setUp(self):
        self.username = 'lubo'
        self.password = 'pwd'
        self.roles = [UserRole.ADMINISTRATOR]
        self.user_manager = UserManager(RamDataPersistenceManager())
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

if __name__ == '__main__':
    unittest.main()
