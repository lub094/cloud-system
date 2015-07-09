from CloudServiceRegistry import CloudServiceRegistry

__author__ = 'Lubo'


class LinuxCloudServiceRegistry(CloudServiceRegistry):
    @staticmethod
    def say_hello():
        print("Hello from the Linux cloud system!")
