#!/usr/bin/python3
"""This is a module for the makeChange function"""


def makeChange(coins, total):
    """a function to determine the fewest number
        of coins needed to meet a given amount total
    """
    cache = [float('inf')] * (total + 1)
    cache[0] = 0

    for amnt in range(1, total + 1):
        for coin in coins:
            if coin <= amnt:
                cache[amnt] = min(cache[amnt], cache[amnt - coin] + 1)

    if cache[total] == float('inf'):
        return -1
    else:
        return cache[total]
