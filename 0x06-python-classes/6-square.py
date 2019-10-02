#!/usr/bin/python3
"""Define the square class"""


class Square:
    """Private instance attribute: size"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        """Return the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """return the position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position value"""
        if type(value) is not tuple or len(value) != 2 or type(value[0]) !=\
           int or type(value[1]) != int or type(value[0]) < 0 or\
           type(value[1]) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

        def area(self):
            """calculate square area"""
            return (self.__size * self.__size)

    def my_print(self):
        """prints square"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                        print("{}". format("-"), end="")
                for j in range(self.__size):
                        print("{}". format("#"), end="")
                print()
