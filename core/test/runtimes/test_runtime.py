import sys
sys.path.append('X:\OneDrive\Programming\Code\Python\Projects\CloudSystem\cloud-system')

import unittest
from core.main.runtimes.runtime import Runtime


class TestRuntime(unittest.TestCase):

    def setUp(self):
        self.id = 1
        self.description = 'description'
        self.owner = 'some owner'  # create a mock owner
        self.runtime = Runtime(None, None, None)

    def tearDown(self):
        pass

    def test_init(self):
        self.runtime = Runtime(self.id, self.description, self.owner)

        self.assertEqual(self.id, self.runtime.get_id())
        self.assertEqual(self.description, self.runtime.get_description())
        self.assertEqual(self.owner, self.runtime.get_owner())

    def test_id_set_and_get(self):
        self.runtime.set_id(self.id)
        self.assertEqual(self.runtime.get_id(), self.id)

    def test_description_set_and_get(self):
        self.runtime.set_description(self.description)
        self.assertEqual(self.runtime.get_description(), self.description)

    def test_owner_set_and_get(self):
        self.runtime.set_owner(self.owner)
        self.assertEqual(self.runtime.get_owner(), self.owner)

    def test_str(self):
        self.assertEqual(str(self.runtime), 'None None None')

if __name__ == '__main__':
    unittest.main()
