#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    length = len(matrix)
    matrixSquare = []

    for rows in range(length):
        matrixSquare.append([])
        # matrixSquare[[]]
        for colum in range(len(matrix[rows])):
            matrixSquare[rows].append(matrix[rows][colum]*matrix[rows][colum])
            # matrix[[1,4,9]...]
    return matrixSquare


"""Other form
def square_matrix_simple(matrix=[]):
    matrixSquare = []
    for rows in matrix:
        square = []
        for columns in rows:
            square.append(columns * columns)
        matrixSquare.append(square)
    return matrixSquare """
