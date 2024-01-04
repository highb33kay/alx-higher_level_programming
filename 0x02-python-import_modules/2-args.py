#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1

print("{} argument{}{}{}".format(
    num_args,
    's' if num_args != 1 else '',
    ':' if num_args > 0 else '.',
    '\n' if num_args > 0 else ''
))

for i, arg in enumerate(argv[1:], start=1):
    print("{}: {}".format(i, arg))
