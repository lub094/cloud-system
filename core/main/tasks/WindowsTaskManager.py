from tasks.Task import Task
from tasks.TaskManager import TaskManager

__author__ = 'Lubo'


class WindowsTaskManager(TaskManager):
    def __init__(self):
        self.arguments = ""
        self.batLocation = ""
        self.description = ""
        self.successfull = True
        self.task = Task()

