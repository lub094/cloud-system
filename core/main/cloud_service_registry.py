class CloudServiceRegistry:

    def __init__(self, binary_manager, task_manager,
                 process_manager, runtime_manager, temporary_files_direcotry):
        self.__binary_manager = binary_manager
        self.__task_manager = task_manager
        self.__process_manager = process_manager
        self.__runtime_manager = runtime_manager
        self.__temporary_files_directory = temporary_files_direcotry

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
