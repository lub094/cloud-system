from binaries.Binary import Binary
from runtimes.Runtimes import Runtime

__author__ = 'Lubo'


class Task:
    def __init__(self):
        self.id = 0
        self.runtime = Runtime()
        self.binary = Binary()
