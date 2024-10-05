#!/usr/bin/python3
"""
Maria and Ben play x rounds of a game where they choose primes from 1 to n.
"""

def sieve_of_eratosthenes(n):
    """Generates a list indicating prime numbers up to n."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, n + 1, i):
                sieve[multiple] = False
    return sieve


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
    for i in range(x):
        n = nums[i]
        prime_count = 0
        if n < 2:
            ben_wins += 1
            continue
        prime_list = sieve_of_eratosthenes(n)
        for m in prime_list:
            if m:
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
