import argparse
import sys

args_from_the_command_line = input('input command: ')
sys.argv = args_from_the_command_line.split(sep=' ')

parser = argparse.ArgumentParser()

parser.add_argument('-s', '--something', required=True)
parser.add_argument('-a', '--anything')

args = parser.parse_args()

raise SystemExit(0)

parser.add_argument('echo', help='some text that is going to be printed')
parser.add_argument('square', help='value to be squared', type=int)
parser.add_argument(
    '--verbose', '-v', help='just saying sth', action='store_true')
parser.add_argument('-print', '-p')

args = parser.parse_args()
print(args.echo)
print(args.square)
print(args.verbose)
print(args.print)

sys.argv = [sys.argv[0], '-h']

args = parser.parse_args()

print(args.echo)
print(args.square)
print(args.verbose)
print(args.print)
