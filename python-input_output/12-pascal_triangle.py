#!/usr/bin/python3

def pascal_triangle(n):
    """_summary_

    Args:
        n (int)

    Returns:
        List: Returns a list of lists of integers representing
        the Pascal’s triangle of n
    """
    pascal = []
    if n <= 0:
        return pascal
    for i in range(n):
        row = [1]
        if i > 0:
            prev = pascal[i - 1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
        pascal.append(row)
    return pascal
