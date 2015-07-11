from core.main.CloudServiceRegistry import CloudServiceRegistry


class WindowsCloudServiceRegistry(CloudServiceRegistry):

    @staticmethod
    def say_hello():
        print("Hello from the Windows cloud system!")
