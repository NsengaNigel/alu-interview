#!/usr/bin/python3
"""
Module to calculate the amount of rainwater retained
after it rains based on wall heights.
"""

def rain(walls):
    """
    Calculate the total amount of rainwater retained.

    Args:
        walls (list): A list of non-negative integers representing wall heights.

    Returns:
        int: The total amount of rainwater retained.
    """
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n
    water = 0

    # Fill left_max array
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Fill right_max array
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate water trapped
    for i in range(n):
        water += min(left_max[i], right_max[i]) - walls[i]

    return water
