#!/usr/bin/python3
"""
square module - prints square
"""
class Square:
    """
    class square that defines square based on file 2
    """
    def __init__(self, size=0):
        """
        module __init__ for size square intialization
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        current square area
        """
        return(self.__size ** 2)
