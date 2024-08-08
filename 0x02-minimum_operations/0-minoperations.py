#!/usr/bin/python3
""" Module to calculates the fewest number of operations needed
to result in exactly n H characters in the file."""


def minOperations(n):
    """
    Calculate the minimum number of operations to reach exactly `n` characters
    starting with one character using **Copy All** and **Paste** operations.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations needed to reach `n` characters.
             Returns 0 if `n` is 1 or less.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
