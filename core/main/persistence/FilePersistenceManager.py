from persistence.PersitenceManager import PersistenceManager

__author__ = 'Lubo'


class FilePersistenceManager(PersistenceManager):
    def __init__(self):
        self.files_location = ""

    def execute_reversible_operation(self):
        pass

    def delete_element(self):
        pass

    def read_element(self):
        pass

    def update_element(self):
        pass

    def get_all_elements(self):
        pass
