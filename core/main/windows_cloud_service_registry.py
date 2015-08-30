from core.main.cloud_service_registry import CloudServiceRegistry


class WindowsCloudServiceRegistry(CloudServiceRegistry):

    @staticmethod
    def say_hello():
        print("Hello from the cloud system on Windows!")
