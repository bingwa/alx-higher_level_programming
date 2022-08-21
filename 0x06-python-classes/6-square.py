#!/usr/bin/python3
"""
square module - printing squares for all your needs
"""
class Square:
    """
    square class for square objects
    """
    #intialization with optional size and optional position
    def __init__(self, size=0, position=(0, 0)):
        """
        initialization
        """
        self.szie = size
        self.position = position

    @property
    #private attributed instance: size
    def size(self):
        """
        size getter for square
        """
        return (self.__size)

    #create the private variable
    @size.setter
    def size(self, value):
        """
        size setter for square
        """
        #calling the setter
        self.__check_size__(value)
        self.__size = value

    #private attribute instance attribute: position
    @property
    def position(self):
        """
        size getter for square
        """
        return (self.__position)

    #property setter def position(self, value)
    @position.setter
    def position(self, value):
        """
        position setter for square
        """
        #for it to be set:
        #it must be an integer i.e. the size
        self.__check_pos__(value)
        #size is less than 0
        self.__position = value

    # Public instance method:
    def area(self):
        """
        returns square's area
        """
        return (self.__size ** 2)

    # Public instance method, could do it with join as well:
    def my_print(self):
        """
        prints a square, prints new line only if size = 0,
        it includes psotion to print them at
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
                for j in range(self.__size):
                    for h in range(self.__position[0]):
                         print(" ", end="")
                         for k in range(self.__size):
                              if k == (self.size - 1):
                                  print("#")
                                  break
                              print("#", end="")
    # create a new attribute in python
    def __check_pos__(self, position):
        """
        error chechking for square position,
        position must be a tuple of 2 integers that are positive
        """
        if (type(position) != tuple or len(position) != 2 or
                type(position[0]) != int or type(position[1]) != int or
                    position[0] < 0 or position[1] < 0):
                # otherwise, raise a TypeError
                raise TypeError("position must be a tuple of 2 positive integers")

    def __check_size__(self, size):
        """
        error chechking for square sizes,
        must be a valid integer, >= 0
        """
        # size must be an integer, otherwise raise a TypeError exception
        if type(size) != int:
            raise TypeError("size must be an integer")
        # if size is less than 0, raise a ValueError
        if size < 0:
            raise ValueError("size must be >= 0")
