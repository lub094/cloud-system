import unittest
from core.main.processes.process import Process


class TaskMock:

    def is_web_task(self):
        return True

    def get_id(self):
        return 0


class TestProcess(unittest.TestCase):

    def setUp(self):
        self.pid = 1
        self.description = 'description'
        self.runtime_location = 'location'
        self.task = TaskMock  # Mock Task through a framework
        self.port = 0
        self.process = Process(None, None, None, None, None)

    def tearDown(self):
        pass

    def test_init(self):
        self.process = Process(self.pid, self.description,
                               self.runtime_location, self.task, self.port)

        self.assertEqual(self.pid, self.process.get_pid())
        self.assertEqual(self.description, self.process.get_description())
        self.assertEqual(self.runtime_location,
                         self.process.get_runtime_location())
        self.assertEqual(self.task, self.process.get_task())
        self.assertEqual(self.port, self.process.get_port())

    def test_pid_set_and_get(self):
        self.process.set_pid(self.pid)
        self.assertEqual(self.process.get_pid(), self.pid)

    def test_description_set_and_get(self):
        self.process.set_description(self.description)
        self.assertEqual(self.process.get_description(), self.description)

    def test_runtime_location_set_and_get(self):
        self.process.set_runtime_location(self.runtime_location)
        self.assertEqual(self.process.get_runtime_location(),
                         self.runtime_location)

    def test_task_set_and_get(self):
        self.process.set_task(self.task)
        self.assertEqual(self.process.get_task(), self.task)

    def test_port_set_and_get(self):
        self.process.set_port(self.port)
        self.assertEqual(self.process.get_port(), self.port)

    def test_str(self):
        self.process.set_task(self.task)
        self.assertEqual(str(self.process), 'None WEB 0 None')

if __name__ == '__main__':
    unittest.main()
