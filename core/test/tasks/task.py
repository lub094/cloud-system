import sys
sys.path.append('X:\OneDrive\Programming\Code\Python\Projects\CloudSystem\cloud-system')

import unittest
from core.main.tasks.task import Task


class BinaryMock:
    def get_id(self):
        return 0

    def is_web_binary(self):
        return False


class RuntimeMock:
    def get_id(self):
        return 1


class TestTask(unittest.TestCase):

    def setUp(self):
        self.id = 1
        self.description = 'description'
        self.owner = 'some owner'  # create a mock owner
        self.binary = BinaryMock()  # create a mock task trough a framework
        self.runtime = RuntimeMock()  # create a mock runtime
        self.task = Task(self.id, self.runtime, self.binary, self.description,
                         self.owner)

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.description, self.task.get_description())
        self.assertEqual(self.owner, self.task.get_owner())
        self.assertEqual(self.runtime.get_id(), self.task.get_runtime_id())
        self.assertEqual(self.binary.get_id(), self.task.get_binary_id())

    def test_description_set_and_get(self):
        self.assertEqual(self.task.get_description(), self.description)

    def test_owner_set_and_get(self):
        self.assertEqual(self.task.get_owner(), self.owner)

    def test_runtime_set_and_get(self):
        self.assertEqual(self.task.get_runtime_id(), self.runtime.get_id())

    def test_binary_set_and_get(self):
        self.assertEqual(self.task.get_binary_id(), self.binary.get_id())

    def test_is_web_task(self):
        self.assertEqual(self.task.is_web_task(), False)

unittest.main()
