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
        available = list(range(1, n + 1))  # Create a list of numbers from 1 to n
        turn = 0  # Maria starts first (turn 0 for Maria, 1 for Ben)
        
        while True:
            # Find the first available prime
            prime_found = False
            for num in available:
                if is_prime(num):
                    prime = num
                    prime_found = True
                    break
            
            if not prime_found:
                # No more primes to pick, current player loses
                if turn % 2 == 0:
                    ben_wins += 1  # Maria's turn, Ben wins
                else:
                    maria_wins += 1  # Ben's turn, Maria wins
                break
            
            # Remove the prime and its multiples from the available numbers
            available = [num for num in available if num % prime != 0]
            
            # Switch turn (0 for Maria, 1 for Ben)
            turn += 1

    # Determine who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
