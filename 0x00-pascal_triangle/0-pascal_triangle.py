#!/usr/bin/python3
"""
Returns a list of lists of intergers rep Pascals triangle
"""


def pascal_triangle(n):
    """
    Pascals triangle in python
    
    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: List of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for k in range(1, i):
            row.append(triangle[i - 1][k - 1] + triangle[i - 1][k])
        row.append(1)
        triangle.append(row)
    return triangle
