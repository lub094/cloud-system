import sys
sys.path.append('X:\OneDrive\Programming\Code\Python\Projects\CloudSystem\cloud-system')

import unittest
from core.main.binaries.binary import Binary


class TestBinary(unittest.TestCase):

    def setUp(self):
        self.id = 1
        self.description = 'description'
        self.owner = 'some owner'  # create a mock owner
        self.file_extension = 'jar'
        self.is_web_binary = False
        self.binary = Binary(None, None, None, None, None)

    def tearDown(self):
        pass

    def test_init(self):
        self.binary = Binary(self.id, self.description, self.owner,
                             self.file_extension, self.is_web_binary)

        self.assertEqual(self.id, self.binary.get_id())
        self.assertEqual(self.description, self.binary.get_description())
        self.assertEqual(self.owner, self.binary.get_owner())
        self.assertEqual(self.file_extension, self.binary.get_file_extension())
        self.assertEqual(self.is_web_binary, self.binary.is_web_binary())

    def test_id_set_and_get(self):
        self.binary.set_id(self.id)
        self.assertEqual(self.binary.get_id(), self.id)

    def test_description_set_and_get(self):
        self.binary.set_description(self.description)
        self.assertEqual(self.binary.get_description(), self.description)

    def test_owner_set_and_get(self):
        self.binary.set_owner(self.owner)
        self.assertEqual(self.binary.get_owner(), self.owner)

    def test_file_extension_set_and_get(self):
        self.binary.set_file_extension(self.file_extension)
        self.assertEqual(self.binary.get_file_extension(), self.file_extension)

    def test_is_web_binary_set_and_get(self):
        self.binary.set_is_web_binary(self.is_web_binary)
        self.assertEqual(self.binary.is_web_binary(), self.is_web_binary)

    def test_str(self):
        self.assertEqual(str(self.binary), 'None None None None')

unittest.main()
