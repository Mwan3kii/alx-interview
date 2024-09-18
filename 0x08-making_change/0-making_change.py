#!/usr/bin/python3
"""Determines fewest numbers of coins needed to meet total"""


def makeChange(coins, total):
    """Return fewest no of coins needed to meet total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
            if dp[total] != float('inf'):
                return dp[total]
    return dp[total] if dp[total] != float('inf') else -1
