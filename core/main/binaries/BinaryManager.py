from core.main.Constants import Constants
from core.main.persistence import PersistenceValidationError
from core.main.persistence.PersistenceExecutionError import \
    PersistenceExecutionError
from core.main.binaries.BinaryExecutionError import BinaryExecutionError
from core.main.tasks import TaskExecutionError
from core.main.binaries.BinaryValidationError import BinaryValidationError
from core.main.persistence.FilePersistenceManager import FilePersistenceManager


class BinaryManager:

    _READ_FAIL_MESSAGE = 'Binary read failed: '
    _DEPLOY_FAIL_MESSAGE = 'Binary deployment failed: '
    _DELETE_FAIL_MESSAGE = 'Binary deletion failed: '

    def __init__(self, data_persistence_manager, binaries_location,
                 cloud_service_registry):
        self.__binaries_location = binaries_location
        self.__cloud_service_registry = cloud_service_registry
        self.__data_persistence_manager = data_persistence_manager
        self.__file_persistence_manager = FilePersistenceManager(
            binaries_location)

    def _get_binary_file_name(self, binary):
        return Constants.BINARY_FILE_FORMAT.format(
            binary.get_id(), binary.get_file_extension())

    def _update_binary_file(self, binary, source_file):
        try:
            binary_source_file_name = self._get_binary_file_name(binary)
            reversible_operation = self.__file_persistence_manager. \
                create_reversible_operation()

            reversible_operation.update_element(binary_source_file_name)
            try:
                self.__data_persistence_manager.update_element(
                    binary.get_id(), binary)
            except (PersistenceExecutionError, PersistenceValidationError) as \
                    e:
                reversible_operation.reverse_changes()
                raise e
        except PersistenceExecutionError as e:
            raise BinaryExecutionError(self._DEPLOY_FAIL_MESSAGE + str(e))
        except PersistenceValidationError as e:
            raise BinaryValidationError(self._DEPLOY_FAIL_MESSAGE + str(e))

    def _used_by_task(self, binary_id):
        try:
            for task in self.__cloud_service_registry.get_task_manager(
            ).get_all_tasks():
                if task.get_binary_id() == binary_id:
                    return True

        except TaskExecutionError:
            return True

        return False

    def _create_binary(self, binary, source_file):
        try:
            destination_file = self._get_binary_file_name(binary)
            reversible_operation = self.__file_persistence_manager. \
                create_reversible_operation()

            reversible_operation.create_element(destination_file)
            try:
                self.__data_persistence_manager.create_element(
                    binary.get_id(), binary)
            except (PersistenceExecutionError, PersistenceValidationError) as \
                    e:
                reversible_operation.reverse_changes()
                raise e
        except PersistenceExecutionError as e:
            raise BinaryExecutionError(self._DEPLOY_FAIL_MESSAGE + str(e))
        except PersistenceValidationError as e:
            raise BinaryValidationError(self._DEPLOY_FAIL_MESSAGE + str(e))

    def read_binary(self, binary_id):
        try:
            return self.__data_persistence_manager.read_element(binary_id)
        except PersistenceValidationError as e:
            raise BinaryValidationError(self._READ_FAIL_MESSAGE + str(e))
        except PersistenceExecutionError as e:
            raise BinaryExecutionError(self._READ_FAIL_MESSAGE + str(e))

    def delete_binary(self, binary_id, user):
        try:
            binary = self.read_binary(binary_id)

            if binary.get_username() != user:
                raise BinaryValidationError(self._DELETE_FAIL_MESSAGE +
                                            'Binaries can only be deleted by \
                                            their owner.')

            if self._used_by_task(binary_id):
                raise BinaryValidationError(self._DELETE_FAIL_MESSAGE +
                                            'Can\'t delete binary that is a \
                                            part of a task')
            binary_file_name = self._get_binary_file_name(binary)
            reversible_operation = self.__file_persistence_manager. \
                create_reversible_operation(binary_file_name)

            reversible_operation.delte_element()
            try:
                self.__file_persistence_manager.delete_element(binary_id)
            except (PersistenceExecutionError, PersistenceValidationError) as \
                    e:
                reversible_operation.reverse_change()
                raise e
            reversible_operation.apply_change()
        except PersistenceValidationError as e:
            raise BinaryValidationError(self._DELETE_FAIL_MESSAGE + str(e))
        except PersistenceExecutionError as e:
            raise BinaryExecutionError(self._DELETE_FAIL_MESSAGE + str(e))

    def deploy_binary(self, binary_id, source_file_name, description, owner):
        source_file = open(source_file_name, 'r')

        try:
            target_binary = self.read_binary(binary_id)

            if target_binary.get_owner() is not owner:
                raise BinaryValidationError('Binaries can only be updated by \
                their owner')

            self._update_binary_file(target_binary, source_file)
        except BinaryValidationError:
            self._create_binary(target_binary, source_file)

    def get_repo_location(self):
        return self.__binaries_location

    def get_all_binaries(self):
        try:
            self.__data_persistence_manager.get_all_elements()
        except PersistenceExecutionError as e:
            raise BinaryExecutionError('Could not get all binaries' + str(e))
