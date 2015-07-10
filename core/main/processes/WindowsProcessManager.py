from processes.ProcessExecutionError import ProcessExecutionError
from persistence.PersistenceExecutionError import PersistenceExecutionError


class WindowsProcessManager:

    _CREATION_FAIL_MESSAGE = 'Process creation failed: '

    _KILL_FAIL_MESSAGE = 'Process killing failed: '

    _PID_ACQUIREMENT_FAIL_MESSAGE = 'Could not acquire pid from the operating \
        system: '

    def __init__(self, data_persistence_manager, temp_files_directory):
        self.__data_persistence_manager = data_persistence_manager
        self.temp_files_directory = temp_files_directory

    def _get_standard_app_pid(self):
        # TODO: finish last
        pass

    def get_active_processes(self):
        # self._clean_processes()

        try:
            return self.__data_persistence_manager.get_all_elements()
        except PersistenceExecutionError as e:
            raise ProcessExecutionError('Could not get processes: ' + str(e))

    def start_process(self):
        pass

    def is_process_active(self):
        pass

    def kill_process(self):
        pass
