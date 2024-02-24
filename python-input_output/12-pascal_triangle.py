#!/usr/bin/python3

"""
Module that returns a
    list of lists of integers
    representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    function def pascal_triangle(n): that returns a
    list of lists of integers
    representing the Pascal’s triangle of n

    Args:
        n (int)

    Returns:
        List: Returns a list of lists of integers representing
        the Pascal’s triangle of n
    """
    pascal = []
    if n <= 0:
        return pascal
    for index in range(n):
        content = [1]
        if index > 0:
            prev = pascal[index - 1]
            for numbers in range(1, index):
                content.append(prev[numbers - 1] + prev[numbers])
            content.append(1)
        pascal.append(content)
    return pascal
