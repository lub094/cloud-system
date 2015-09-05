from core.main.users.user_manager import UserManager


class WindowsCloudServiceRegistry:

    def __init__(self, data_persistence_manager):
        self.__user_manager = UserManager(data_persistence_manager)
        # self.binary_manager = BinaryManager()
        # self.task_manager = WindowsTaskManager()
        # self.process_manager = WindowsProcessManager()
        # self.runtime_manager = RuntimeManager()

    def get_temporary_files_directory(self):
        return self.__temporary_files_directory

    def get_task_manager(self):
        return self.__task_manager

    def get_binary_manager(self):
        return self.__binary_manager

    def get_process_manager(self):
        return self.__process_manager

    def get_runtime_manager(self):
        return self.__runtime_manager

    def get_user_manager(self):
        return self.__user_manager
