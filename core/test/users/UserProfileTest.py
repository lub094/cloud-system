import unittest
from core.main.users.UserRole import UserRole
from core.main.users.UserProfile import UserProfile


class UserProfileTest(unittest.TestCase):

    username = 'admin'
    password = 'pass'
    roles = [UserRole.BASIC, UserRole.ADMINISTRATOR]

    def test_init(self):
        user = UserProfile(self.username, self.password, self.roles)

        self.assertEquals(user.get_username(), self.username)
        self.assertEquals(user.get_roles(), self.roles)

    def test_add_role(self):
        role = UserRole.ADMINISTRATOR
        user = UserProfile(self.username, self.password, [])
        user.add_role(role)

        self.assertTrue(user.is_in_role(role))

    def test_add_roles(self):
        roles = [UserRole.ADMINISTRATOR, UserRole.BASIC]
        user = UserProfile(self.username, self.password, [])
        user.add_roles(roles)

        for role in roles:
            self.assertTrue(user.is_in_role(role))

if __name__ == '__main__':
    unittest.main()
