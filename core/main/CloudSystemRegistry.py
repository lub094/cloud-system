__author__ = 'Lubo'


class CloudSystemRegistry:
    def __init__(self):
        self.binary_manager = None
        self.task_manager = None
        self.process_manager = None
        self.runtime_manager = None
        self.temporary_files_directory = ""

    def get_temporary_files_directory(self):
        return self.temporary_files_directory
