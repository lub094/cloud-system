class Binary:
    def __init__(self, id_, description, owner, file_extension, is_web_binary):
        self.__id = id_
        self.__description = description
        self.__owner = owner
        self.__file_extension = file_extension
        self.__is_web_binary = is_web_binary

    def get_description(self):
        return self.__description

    def get_id(self):
        return self.__id

    def get_owner(self):
        return self.__owner

    def get_file_extension(self):
        return self.__file_extension

    def is_web_binary(self):
        return self.__is_web_binary

    def set_description(self, description):
        self.__description = description

    def set_id(self, id_):
        self.__id = id_

    def set_owner(self, owner):
        self.__owner = owner

    def set_file_extension(self, file_extension):
        self.__file_extension = file_extension

    def set_is_web_binary(self, is_web_binary):
        self.__is_web_binary = is_web_binary

    def __str__(self):
        return "{} {} {} {}".format(self.__id, self.__file_extension,
                                    self.__owner, self.__description)
