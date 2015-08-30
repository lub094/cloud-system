class Process:
    def __init__(self, pid, description, runtimes_location, task, port):
        self.__pid = pid
        self.__description = description
        self.__runtime_location = runtimes_location
        self.__task = task
        self.__port = port

    def get_pid(self):
        return self.__pid

    def get_description(self):
        return self.__description

    def get_runtime_location(self):
        return self.__runtime_location

    def get_task(self):
        return self.__task

    def get_port(self):
        return self.__port

    def set_pid(self, pid):
        self.__pid = pid

    def set_description(self, description):
        self.__description = description

    def set_runtime_location(self, runtime_location):
        self.__runtime_location = runtime_location

    def set_task(self, task):
        self.__task = task

    def set_port(self, port):
        self.__port = port

    def is_web_app(self):
        return self.__task.is_web_task(self.__task)

    def __str__(self):
        process_type = "WEB" if self.is_web_app() else "DESKTOP"
        return "{} {} {} {}".format(self.__pid, process_type,
                                    self.__task.get_id(self.__task),
                                    self.__description)
