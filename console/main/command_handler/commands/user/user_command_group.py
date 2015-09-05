import argparse
from console.main.command_handler.command_type import CommandType


class UserCommandGroup:

    def __init__(self, args):
        self.__commands = ['create', 'delete', 'print-all']
        self.__groups = ['role']
        self.__command = None

        self.__args = args
        self.__parser = argparse.ArgumentParser('Users command group')
        self.__parser.add_argument(
            'command', choices=self.__commands + self.__groups)
        self.__parser.add_argument('unparsed', nargs='*')

    def get_parsed_child(self):
        try:
            args_namespace = self.__parser.parse_args(self.__args)
        except SystemExit:
            return self

        if args_namespace.command == 'role':
            return None  # create role command group
        elif args_namespace.command in ['create', 'delete', 'read',
                                        'print-all', '-h', '--help']:
            self.__command = args_namespace.command
            return self

    def get_command(self):
        if self.__command == 'create':
            return CommandType.USER_CREATE
        elif self.__command == 'delete':
            return CommandType.USER_DELETE
        elif self.__command == 'print-all':
            return CommandType.USER_PRINT_ALL
