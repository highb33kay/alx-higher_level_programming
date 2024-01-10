#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calculator(a, operator, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Invalid input. Please provide integers for 'a' and 'b'.")
        sys.exit(1)

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print(f"{a} {operator} {b} = {result}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]

    calculator(a, operator, b)
