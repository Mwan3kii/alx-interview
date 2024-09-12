#!/usr/bin/python3
"""Rotate 2d matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Take n x n 2D matrix and rotate it 90 degress clockwise"""
    n = len(matrix)
    for r in range(n):
        for c in range(r, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    for row in range(n):
        matrix[row].reverse()
