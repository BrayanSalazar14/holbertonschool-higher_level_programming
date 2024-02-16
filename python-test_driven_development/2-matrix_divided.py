#!/usr/bin/python3
"""
This is the "matrix_divided" module.
The add module supplies one function, matrix_divided().  For example,
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
"""
def matrix_divided(matrix, div):
    """Returns an new matrix:
    With all elements of the matrix divided by div
    """
    if type(div) == int or type(div) == float:
        if div != 0:
            newMatrix = []
            for rows in range(len(matrix)):
                newMatrix.append([])
                for columns in matrix[rows]:
                    if isinstance(columns, (int, float)):
                        newMatrix[rows].append(round((columns / div), 2))
                    else:
                        raise TypeError("matrix must be a matrix " +
                                        "(list of lists) of integers/floats")
            if len(matrix) == len(newMatrix):
                return newMatrix
            else:
                raise TypeError("Each row of the matrix " +
                                "must have the same size")
        else:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")
