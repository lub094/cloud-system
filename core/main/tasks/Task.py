from core.main.constants import Constants


class Task:

    def __init__(self, id_, runtime, binary, description, owner):
        self.__id = id_
        self.__runtime = runtime
        self.__binary = binary
        self.__description = description
        self.__owner = owner

    def get_binary_id(self):
        return self.__binary.get_id()

    def get_description(self):
        return self.__description

    def get_owner(self):
        return self.__owner

    def get_runtime_id(self):
        return self.__runtime.get_id()

    def get_execution_filename(self):
        return Constants.TASK_RUN_FILE_FORMAT.format(self.__id,
                                                     self.get_runtime_id(),
                                                     self.get_binary_id())

    def is_web_task(self):
        return self.__binary.is_web_binary()
