from console.main.command_handler.command_line_handler import \
    CommandLineHandler


class CloudSystemApp:

    def __init__(self, cloud_service_registry):
        self.__cloud_service_registry = cloud_service_registry

    def run_interactive_mode(self):
        print(' == STARTING INTERACTIVE MODE == \n')

        command_line_handler = CommandLineHandler(
            self.__cloud_service_registry)
        command_line_handler.print_root_help()

        args = []

        while 'exit' not in args:
            args = input('\ninput command: ').split(sep=' ')
            command_line_handler.execute(args)

        print('\n == EXITING INTERACTIVE MODE ==')
