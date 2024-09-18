#!/usr/bin/python3
"""Determines fewest numbers of coins needed to meet total"""


def makeChange(coins, total):
    """Return fewest no of coins needed to meet total"""
    if total <= 0:
        return 0
    curr_total = 0
    used_coins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        dp = (total - curr_total) // coin
        curr_total += dp * coin
        used_coins += dp
        if curr_total == total:
            return used_coins
    return -1
