import argparse
from console.main.command_handler.commands.user.user_command_group import \
    UserCommandGroup
from console.main.command_handler.command_type import CommandType


class CloudSystemCommandGroup:

    def __init__(self, args):
        self.__groups = ['user', 'binary', 'runtime', 'task', 'process']
        self.__commands = ['exit']

        self.__args = args
        self.__command = None

        self.parser = argparse.ArgumentParser('The cloud system application')
        self.parser.add_argument(
            'command', choices=self.__commands + self.__groups)
        self.parser.add_argument('unparsed', nargs='*')

    def get_parsed_child(self):
        try:
            args_namespace = self.parser.parse_args(self.__args)
        except SystemExit:
            return self

        if args_namespace.command == 'user':
            return UserCommandGroup(args_namespace.unparsed)
        elif args_namespace.command in self.__commands:
            self.__command = args_namespace.command
            return self
        else:
            raise Exception('unimplemented')

    def get_command(self):
        if self.__command == 'exit':
            return CommandType.EXIT
