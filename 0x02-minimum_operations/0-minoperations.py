#!/usr/bin/python3
""" Calculates the fewest number of operations
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """ Calculates the fewest number of operations needed
        to result in exactly n H characters in the file.

    Args:
        n (int): Number of H characters to reach.
    Returns:
        (int): The fewest number of operations
    """
    if n <= 1:
        return 0
    else:
        x = 2
        operations = 0
        while x <= n:
            if n % x == 0:
                operations += x
                n = n / i
            else:
                x += 1
        return operations
