from CloudServiceRegistry import CloudServiceRegistry


class LinuxCloudServiceRegistry(CloudServiceRegistry):
    @staticmethod
    def say_hello():
        print("Hello from the Linux cloud system!")
