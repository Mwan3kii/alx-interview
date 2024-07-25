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
    if n > 0:
        for i in range(1, n + 1):
            level = []
            row = 1
            for j in range(1, i + 1):
                level.append(row)
                row = row * (i - j) // j
            triangle.append(level)
    return triangle
