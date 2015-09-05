from console.main.command_handler.commands.cloud_system_command_group import \
    CloudSystemCommandGroup
from console.main.command_handler.command_type import CommandType
from core.main.users.user_role import UserRole


class CommandLineHandler:

    def __init__(self, cloud_service_registry):
        self.commands = None
        self.cloud_service_registry = cloud_service_registry
        self.root_command = CloudSystemCommandGroup(['-h'])

        self._users_added = False

    def __add_users(self):
        self.cloud_service_registry.get_user_manager().create_user(
            'admin', 'admin', [UserRole.ADMINISTRATOR])
        self.cloud_service_registry.get_user_manager().create_user(
            'lubo', 'pass', [UserRole.ADMINISTRATOR, UserRole.BASIC])

        self._users_added = True

    def execute(self, args):
        group = CloudSystemCommandGroup(args)
        command = None

        while group:
            group = group.get_parsed_child()

            if group.get_command():
                command = group.get_command()
                group = None

        if command == CommandType.USER_PRINT_ALL:
            if not self._users_added:
                self.__add_users()

            users = self.cloud_service_registry.get_user_manager(
            ).get_all_users()

            print('Users:')
            print('=======================================')
            print('Username | Roles')
            print('---------------------------------------')

            for user in users:
                print(user)

            print('=======================================')
        elif command == CommandType.USER_CREATE:
            pass

    def print_root_help(self):
        try:
            self.root_command.get_parsed_child()
        except SystemExit:
            pass
