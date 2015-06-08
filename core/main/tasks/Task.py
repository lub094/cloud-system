from binaries.Binary import Binary
from runtimes.Runtimes import Runtime
from users.User import User

__author__ = 'Lubo'


class Task:
    def __init__(self):
        self.id = 0
        self.runtime = Runtime()
        self.binary = Binary()
        self.description = str(self.binary.description) + " runnin on " + \
                           str(self.runtime.description)
        self.owner = User()