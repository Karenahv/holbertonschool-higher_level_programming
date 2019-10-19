#!/usr/bin/python3
"""class rectangle"""


from models.base import Base
import sys


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(' ', end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        lenofargs = len(args)
        if lenofargs > 0:
            self.id = args[0]
            lenofargs -= 1
        if lenofargs > 0:
            self.__width = args[1]
            lenofargs -= 1
        if lenofargs > 0:
            self.__height = args[2]
            lenofargs -= 1
        if lenofargs > 0:
            self.__x = args[3]
            lenofargs -= 1
        if lenofargs > 0:
            self.__y = args[4]
        if kwargs:
            for key, value in kwargs.items():
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'id':
                    self.id = value

    def to_dictionary(self):
        dic1 = {}
        for key, value in self.__dict__.items():
            if 'x' in key:
                dic1['x'] = value
            if 'y' in key:
                dic1['y'] = value
            if 'id' in key:
                dic1['id'] = value
            if 'width' in key:
                dic1['width'] = value
            if 'height' in key:
                dic1['height'] = value
        return dic1
