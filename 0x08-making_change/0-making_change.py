def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.
    Args:
        coins: A list of distinct integers representing coin denominations.
        total: The total amount for which change is to be made.
    Returns:
        The minimum number of coins to make up the total.or -1 if not possible.
    """
    if total <= 0:
        return 0
    n = len(coins)
    number = 0
    i = n - 1
    while(i >= 0):
        while (total >= coins[i]):
            total -= coins[i]
            number += 1
        i -= 1
    if total != 0 or number == 0:
        return -1
    return number
