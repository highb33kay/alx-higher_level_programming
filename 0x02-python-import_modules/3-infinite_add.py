#!/usr/bin/python3
from sys import argv

result = sum(int(arg) for arg in argv[1:])

print(result)
