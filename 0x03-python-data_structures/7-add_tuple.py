#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Use the value 0 for missing integers and only consider the first 2 integers
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Perform element-wise addition
    result = (a[0] + b[0], a[1] + b[1])

    return result
