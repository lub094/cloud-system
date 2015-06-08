from tasks.Task import Task

__author__ = 'Lubo'


class Process:
    def __init__(self):
        self.pid = 0
        self.description = ""
        self.runtime_location = ""
        self.task = Task()
