#!/usr/bin/python3
"""
Maria and Ben play x rounds of a game where they choose primes from 1 to n.
"""


def isWinner(x, nums):
    """
    Determines the player who won the most rounds.
    Args:
        x (int): Number of rounds.
        nums (list of int): List of n values for each round.
    Returns:
        str: "Maria" if Maria wins more rounds, "Ben" if Ben wins, or None.
    """
    maria_wins = 0
    ben_wins = 0
    if nums is None or x < 1:
        return None

    def is_prime(num):
        """Return True if num is prime, else False."""
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    for i in range(x):
        n = nums[i]
        prime_count = 0
        for num in range(2, n + 1):
            if is_prime(num):
                prime_count += 1
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
