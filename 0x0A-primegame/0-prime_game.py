#!/usr/bin/python3
"""
Prime Game: Maria and Ben play x rounds of a game where they choose primes from 1 to n.
Maria starts first. The player that cannot make a move loses.
"""

def isWinner(x, nums):
    """
    Determines the player who won the most rounds.
    
    Args:
        x (int): Number of rounds.
        nums (list of int): List of n values for each round.
    
    Returns:
        str: "Maria" if Maria wins more rounds, "Ben" if Ben wins more rounds, or None if tied.
    """
    maria_wins = 0
    ben_wins = 0

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
        available = list(range(2, n + 1))  # Start with numbers from 2 to n
        turn = 0  # Maria starts first (0 for Maria, 1 for Ben)
        
        while available:
            prime_found = False
            for num in available:
                if is_prime(num):  # Find the first prime
                    prime_found = True
                    # Remove prime and its multiples
                    available = [x for x in available if x % num != 0]
                    break

            if not prime_found:
                # No more primes available
                if turn % 2 == 0:
                    ben_wins += 1  # Maria's turn, Ben wins
                else:
                    maria_wins += 1  # Ben's turn, Maria wins
                break

            # Switch turns
            turn += 1

    # Determine who won more rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None

