#!/usr/bin/python3
"""Can execute only two operations Copy All and Paste"""


def minOperations(n):
    """Result in exactly n H characters in the file"""
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
