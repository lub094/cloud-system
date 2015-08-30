from core.main.persistence.file_persistence_manager import FilePersistenceManager
from core.main.tasks import task_execution_error
from core.main.runtimes.runtime_execution_error import RuntimeExecutionError
from core.main.runtimes.runtime_validation_error import RuntimeValidationError
from core.main.persistence.persistence_validation_error import \
    PersistenceValidationError
from core.main.persistence.persistence_execution_error import \
    PersistenceExecutionError
from core.main.runtimes.runtime import Runtime
from core.main.constants import Constants
from os.path import isfile
import os


class RuntimeManager:

    _CREATE_FAIL_MESSAGE = 'Runtime creation failed: '
    _DELETE_FAIL_MESSAGE = 'Runtime deletion failed: '
    _UPDATE_FAIL_MESSAGE = 'Runtime update failed: '

    def __init__(self, data_persistence_manager, runtimes_location,
                 cloud_service_registry):
        self.__cloud_service_registry = cloud_service_registry
        self.__data_persistence = data_persistence_manager
        self.__runtimes_location = runtimes_location

        self.__files_persistence = FilePersistenceManager(runtimes_location)

        self.__runtimes_id_counter = 0
        self._set_proper_id_counter(self.__data_persistence.get_all_elements())

    def _set_proper_id_counter(self, runtimes):
        self.__runtimes_id_counter = 0
        for runtime in runtimes:
            if runtime.get_id() >= self.__runtimes_id_counter:
                self.__runtimes_id_counter = runtime.get_id()

    def _used_by_task(self, runtime_id):
        try:
            for task in self.__cloud_service_registry.get_task_manager(
            ).get_all_tasks():
                if task.get_runtime_id() == runtime_id:
                    return True
        except task_execution_error as e:
            raise RuntimeExecutionError(
                'Checking if runtime is part of a task has failed.' + str(e))

        return False

    def _get_runtime_source_file(self, file_path, error_message):
        if not isfile(file_path):
            raise RuntimeValidationError(
                error_message +
                'Source file does not exit.')

        source_file = open(file_path, 'w')

        if not self._valid_runtime_extension(file_path):
            raise RuntimeValidationError(
                error_message +
                'File format is not supported.')

        return source_file

    def _get_next_id(self):
        return ++self.__runtimes_id_counter

    def _get_runtime_file_name(self, runtime):
        return Constants.RUNTIME_FILE_FORMAT.format(runtime.get_id(),
                                                    Constants.
                                                    RUNTIME_FILE_EXTENSION)

    def read_runtime(self, runtime_id):
        try:
            return self.__data_persistence.read_element(runtime_id)
        except PersistenceValidationError as e:
            raise RuntimeValidationError(
                'Runtime reading has failed: ' +
                str(e))
        except PersistenceExecutionError as e:
            raise RuntimeExecutionError('Runtime could not be read.')

    def create_runtime(self, file_path, description, owner):
        try:
            source_file = self._get_runtime_source_file(
                file_path,
                self._CREATE_FAIL_MESSAGE)

            runtime_id = self._get_next_id()
            new_runtime = Runtime(runtime_id, description, owner)

            reversible_operation = \
                self.__files_persistence.create_reversible_operation()

            reversible_operation.create_element(source_file)
            try:
                self.__data_persistence.create_element(runtime_id, new_runtime)
            except (PersistenceExecutionError, PersistenceValidationError) as \
                    e:
                reversible_operation.reverse_change()
                raise e
            reversible_operation.apply_change
        except (PersistenceExecutionError, PersistenceValidationError) as e:
            raise RuntimeExecutionError(self._CREATE_FAIL_MESSAGE + str(e))

    def delete_runtime(self, runtime_id, user):
        if self.read_runtime(runtime_id).get_owner() != user:
            raise RuntimeValidationError(
                self._DELETE_FAIL_MESSAGE +
                'Runtimes can only be deleted by their owner')

        if self._used_by_task(runtime_id):
            raise RuntimeValidationError(
                self._DELETE_FAIL_MESSAGE +
                'Can\'t delete a runtime that is a part of a task')

        try:
            deleted_runtime = self.__data_persistence.delete_element(
                runtime_id)
            os.remove(
                self.__runtimes_location +
                self._get_runtime_file_name(deleted_runtime))
        except PersistenceExecutionError as e:
            raise RuntimeExecutionError(str(e))

    def get_repo_location(self):
        return self.__runtimes_location

    def get_all_runtimes(self):
        try:
            return self.__data_persistence.get_all_elements()
        except PersistenceExecutionError as e:
            raise RuntimeExecutionError(
                'Could not get all runtimes: ' +
                str(e))

    def update_runtime(self):
        pass
