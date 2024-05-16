#!/usr/bin/python3
"""This is a module for the Prime game, an interview question"""


def generate_primes(num):
    """a function to generate prime numbers"""
    primes = [True for x in range(num + 1)]
    start = 2
    while (start * start) <= num:
        if primes[start] is True:
            for x in range(start * start, num + 1, start):
                primes[x] = False
        start += 1
    prime_nums = [x for x in range(2, num + 1) if primes[x]]
    return prime_nums


def isWinner(x, nums):
    """determines the winner based on prime numbers and their factors"""
    ben_wins = 0
    maria_wins = 0

    for n in nums:
        primes = generate_primes(n)
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return 'Ben'
    elif maria_wins > ben_wins:
        return 'Maria'
    else:
        return 'None'
