#!/usr/bin/python3
"""
square module - printing squares
"""
class Square:
    """
    class Square defines a square based on file 1
    """
    def __init__(self, size=0):
        """
        module __init__ for size square initialization
        """
        #size must be an integer
        if type(size) is not int:
            #otherwise raise TypeError
            raise TypeError("size must be an integer")
        elif size < 0:
            #if size is less than zero
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
