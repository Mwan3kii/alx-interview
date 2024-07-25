#!/usr/bin/python3
"""Returns a list of lists of intergers rep Pascals triangle"""


def pascal_triangle(n):
    """Returns an empty list if n <= 0"""
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