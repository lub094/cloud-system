from CloudServiceRegistry import CloudServiceRegistry

__author__ = 'Lubo'


class RuntimeManager:
    def __init__(self):
        self.cloud_service_registry = CloudServiceRegistry()
        self.files_persistence = None
        self.data_persistence = None
        self.runtimes_id_counter = 0
        self.runtime_location = ""

    def create_runtime(self):
        pass

    def delete_runtime(self):
        pass

    def get_all_runtimes(self):
        pass

    def get_repo_location(self):
        pass

    def read_runtime(self):
        pass

    def update_runtime(self):
        pass


