#!/usr/bin/python3
"""Prime game between maria and ben"""


def isWinner(x, nums):
    """Determine winner of game each round"""
    if not nums or x <= 0:
        return None
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False

    for m in range(2, int(max_num ** 0.5) + 1):
        if primes[m]:
            for b in range(m * m, max_num + 1, m):
                primes[b] = False

    primes_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        primes_count[i] = primes_count[i - 1] + (1 if primes[i] else 0)

    maria = 0
    ben = 0

    for n in nums:
        if primes_count[n] % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
