import argparse


class UserPrintAllCommand:

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            'Prints the full information of all users.')
        self.parser.add_argument('-P', '--Password', required=True)
        self.parser.add_argument('-U', '--Username', required=True)

    def parse(self, args):
        args_namespace = self.parser.parse_args(args)
        args_namespace.P
