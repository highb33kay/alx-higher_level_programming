#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    
    "sum a and b"
    print("{} + {} = {}".format(a, b, add(a, b)))

    "difference between a and b"
    print("{} - {} = {}".format(a, b, sub(a, b)))

    "multiplying a and b"
    print("{} * {} = {}".format(a, b, mul(a, b)))

    "divide a by b"
    print("{} / {} = {}".format(a, b, div(a, b)))
