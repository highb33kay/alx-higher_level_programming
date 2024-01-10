#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""
    new_matrix = [list(map(lambda x: x**2, row)) for row in matrix]
    return new_matrix
