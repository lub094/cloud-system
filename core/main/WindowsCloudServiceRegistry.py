from CloudServiceRegistry import CloudServiceRegistry

__author__ = 'Lubo'


class WindowsCloudServiceRegistry(CloudServiceRegistry):
    @staticmethod
    def say_hello():
        print("Hello from the Windows cloud system!")
