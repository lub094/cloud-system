from core.main.users.user_manager import UserManager


class LinuxCloudServiceRegistry:

    def __init__(self, data_persistence_manager):
        self.__user_manager = UserManager(data_persistence_manager)
        # self.binary_manager = BinaryManager()
        # self.task_manager = LinuxTaskManager()
        # self.process_manager = LinuxProcessManager()
        # self.runtime_manager = RuntimeManager()

    def get_user_manager(self):
        return self.__user_manager
