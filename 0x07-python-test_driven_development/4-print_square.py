#!/usr/bin/python3
"""prints a square with the character #."""
def print_square(size):
    """prints a square with the character #."""
    # size must be an integer, otherwise raise a TypeError
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for x in range(size):
        print('#' * size)
