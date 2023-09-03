#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: matrix have non-numbers.
        TypeError: matrix have rows of different sizes.
        TypeError: divider not int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        new matrix representing result of division.
    """
    if (not isinstance(matrix, list) or matrix == [] or not
        all(isinstance(r, list) for r in matrix) or not
        all((isinstance(element, int) or isinstance(element, float))
            for element in [n for r in matrix for n in r])):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(len(r) == len(matrix[0]) for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), r)) for r in matrix])
