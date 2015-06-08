from CloudServiceRegistry import CloudServiceRegistry
from persistence.DataPersistenceManager import DataPersistenceManager
from persistence.FilePersistenceManager import FilePersistenceManager

__author__ = 'Lubo'


class BinaryManager:
    def __init__(self):
        self.binaries_location = ""
        self.cloud_service_registry = CloudServiceRegistry()
        self.file_persistence = FilePersistenceManager()
        self.data_persistence = DataPersistenceManager()

    def create_binary(self):
        pass

    def delete_binary(self):
        pass

    def deploy_binary(self):
        pass

    def get_repo_location(self):
        pass

    def used_by_task(self):
        pass
