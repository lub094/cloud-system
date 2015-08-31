from core.main.persistence.persistence_validation_error import PersistenceValidationError
from core.main.users.user_validation_error import UserValidationError


class RamDataPersistenceManager:

    def __init__(self):
        self.__elements = {}

    def update_element(self, key, element):
        if key in self.__elements:
            self.__elements[key] = element
        else:
            raise PersistenceValidationError('Element does not exist')

    def read_element(self, key):
        try:
            return self.__elements[key]
        except:
            raise UserValidationError('Element does not exist')

    def create_element(self, key, element):
        self.__elements[key] = element

    def delete_element(self, key):
        del self.__elements[key]

    def get_all_elements(self):
        return self.__elements.values()
