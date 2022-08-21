#!/usr/bin/python3
"""
square module - prints squares
"""
class Square:
    """
    class square now has getters and setters for size
    """
    def __init__(self, size=0):
        """
        class square take square takes in an int size
        """
        #methods inherited from the class
        self.size = size

    @property
    def size(self):
        """
        size getter returns the private size
        """
        #return current area
        return self.__size

    @size.setter
    def size(self, size):
        """
        sets the size
        """
        #has to be an int value

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        #returns area of square
        return (self.__size ** 2)
