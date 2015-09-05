import unittest
from mock import Mock
from core.main.binaries.binary_manager import BinaryManager
from core.main.constants import Constants


class Test(unittest.TestCase):

    def setUp(self):
        self.file_persistence_manager_mock = Mock()
        self.data_psersistence_manager_mock = Mock()
        self.binary_manager =\
            BinaryManager(self.data_psersistence_manager_mock,
                          self.file_persistence_manager_mock,
                          'test_location')
        self.binary_mock = Mock()
        self.binary_mock.get_id.return_value = 1
        self.binary_mock.get_file_extension.return_value = 'jar'

        self.reversible_operation = Mock()
        self.file_persistence_manager_mock.create_reversible_operation.\
            return_value = self.reversible_operation

    def test_get_binary_file_name(self):
        self.assertEqual(Constants.BINARY_FILE_FORMAT.format(1,
                                                             'jar'),
                         self.binary_manager.
                         _get_binary_file_name(self.binary_mock))

    def test_update_binary_file(self):
        source_file_name = 'test_name'
        self.binary_manager._get_binary_file_name = lambda x:\
            source_file_name

        self.binary_manager._update_binary_file(self.binary_mock, 'test_file')

        self.file_persistence_manager_mock.create_reversible_operation.\
            assert_called_once_with()
        self.reversible_operation.update_element.assert_called_once_with(
            source_file_name)
        self.data_psersistence_manager_mock.update_element.\
            assert_called_once_with(1, self.binary_mock)

    def test_create_binary(self):
        destination_file_name = 'test_dest'
        self.binary_manager._get_binary_file_name = lambda x:\
            destination_file_name

        self.binary_manager._create_binary(
            self.binary_mock, 'test_source')

        self.file_persistence_manager_mock.\
            create_reversible_operation.assert_called_once_with()
        self.reversible_operation.create_element.assert_called_once_with(
            destination_file_name)
        self.data_psersistence_manager_mock.create_element.\
            assert_called_once_with(
                self.binary_mock.get_id(), self.binary_mock)

    def test_read_binary_success(self):
        return_value = 'test'
        self.data_psersistence_manager_mock.read_element.\
            return_value = return_value

        self.assertEqual(return_value, self.binary_manager.read_binary(
            self.binary_mock.get_id()))

        self.data_psersistence_manager_mock.read_element.\
            assert_called_once_with(self.binary_mock.get_id())

    def test_delete_binary(self):
        self.binary_manager.read_binary = lambda x: self.binary_mock
        self.binary_manager._get_binary_file_name = lambda x: 'test_file'
        user_name = 'test_user'
        self.binary_mock.get_username.return_value = user_name

        self.binary_manager.delete_binary(
            self.binary_mock.get_id(), user_name)

        self.reversible_operation.delete_element.assert_called_once_with()

if __name__ == "__main__":
    unittest.main()
