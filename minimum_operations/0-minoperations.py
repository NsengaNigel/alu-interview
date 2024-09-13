#!/usr/bin/python3
"""
Module for calculating the minimum operations needed
to get n 'H' characters in a file.
"""

def minOperations(n):
    """
    Returns the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.
    
    Returns:
        int: The minimum number of operations or 0 if it's not possible.
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
