from tasks.Task import Task
from tasks.TaskManager import TaskManager


class LinuxTaskManager(TaskManager):
    def __init__(self):
        self.arguments = ""
        self.batLocation = ""
        self.description = ""
        self.successfull = True
        self.task = Task()
