#!/usr/bin/python3
"""
square module - prints square
"""
class Square:
    """
    square class with fiunction to print square
    """
    def __init__(self, size=0):
        """
        intitialization for square, takes in int size
        """
        self.__size = size

    @property
    #property define size(self) to retrieve it
    def size(self):
        """
        size getter, returns the private size
        """
        return self.__size

    @size.setter
    #propertysetter def size(self, value) to set it
    def size(self, size):
        """
        size setter, sets the private setter
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    #public instance method
    def area(self):
        """
        returns area of the square
        """
        return (self.size ** 2)

    #public instance method, could do it with join as well
    def my_print(self):
        """
        Prints the square! should only print a newline if size is 0
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    if j == (self.size - 1):
                        print("#")
                        break
                    print("#", end="")
