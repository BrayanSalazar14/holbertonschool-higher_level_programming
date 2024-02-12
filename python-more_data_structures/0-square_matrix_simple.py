#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    length = len(matrix)
    matrixSquare = []

    for rows in range(length):
        matrix2.append([])
        for columns in range(len(matrix[rows])):
            matrixSquare[rows].append(matrix[rows][columns] * matrix[rows][columns])
    return matrix2
