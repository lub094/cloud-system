from core.main.users.UserProfile import UserProfile
from core.main.runtimes.Runtimes import Runtime
import unittest


class RuntimeTest(unittest.TestCase):

    id = 1
    description = 'test description'
    owner = UserProfile()

    def test_init(self):
        runtime = Runtime(self.id, self.description, self.owner)

        self.assertEqual(runtime.get_id(), self.id)
        self.assertEqual(runtime.get_description(), self.description)
        self.assertEqual(runtime.get_owner(), self.owner)

if __name__ == '__main__':
    unittest.main()
