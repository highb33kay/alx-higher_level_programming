#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list."""
    unique_sum = sum(set(my_list))
    return unique_sum
