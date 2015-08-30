import sys
from core.main.users.user_role import UserRole
from core.main.users.user_profile import UserProfile
sys.path.append('X:\OneDrive\Programming\Code\Python\Projects\CloudSystem\cloud-system')

import unittest


class TestUserProfile(unittest.TestCase):

    username = 'uname'
    password = 'pwd'
    roles = [UserRole.ADMINISTRATOR, UserRole.BASIC]

    def setUp(self):
        self.user_profile = UserProfile(self.username, self.password,
                                        self.roles)

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.username, self.user_profile.get_username())
        self.assertEqual(self.roles, self.user_profile.get_roles())
        self.assertTrue(self.user_profile.validate_password(self.password))

    def test_username_set_and_get(self):
        self.assertEqual(self.user_profile.get_username(), self.username)

    def test_roles_set_and_get(self):
        roles = [UserRole.BASIC]
        self.user_profile.set_roles(roles)
        self.assertEqual(roles, self.user_profile.get_roles())

    def test_add_role(self):
        roles = [UserRole.ADMINISTRATOR, UserRole.BASIC]
        self.user_profile.set_roles([])

        for role in roles:
            self.user_profile.add_role(role)

        self.assertEqual(self.user_profile.get_roles(), roles)

    def test_add_roles(self):
        roles = [UserRole.ADMINISTRATOR]
        self.user_profile.set_roles([])
        self.user_profile.add_roles(roles)

        self.assertEquals(self.user_profile.get_roles(), roles)

    def test_str(self):
        self.assertEqual(str(self.user_profile), self.username)

unittest.main()
