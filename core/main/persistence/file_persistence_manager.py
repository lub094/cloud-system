from core.main.persistence.persistence_manager import PersistenceManager


class FilePersistenceManager(PersistenceManager):

    def __init__(self):
        self.files_location = ''

    def create_reversible_operation(self):
        pass

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
