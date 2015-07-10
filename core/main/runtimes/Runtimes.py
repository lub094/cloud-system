class Runtime:

    def __init__(self, id_, description, owner):
        self.__id = id_
        self.__description = description
        self.__owner = owner

    def get_id(self):
        return self.__id

    def get_description(self):
        return self.__description

    def get_owner(self):
        return self.__owner

    def set_description(self, description):
        self.__description = description

    def set_owner(self, owner):
        self.__owner = owner

    def set_id(self, id_):
        self.__id = id_

    def __str__(self):
        return "{} {} {}".format(self.__id, self.__owner, self.__description)
