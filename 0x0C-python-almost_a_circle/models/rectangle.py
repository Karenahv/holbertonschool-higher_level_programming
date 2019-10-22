#!/usr/bin/python3
"""class rectangle"""


from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """class rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """class rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """class rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """class rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """class rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """class rectangle"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """class rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """class rectangle"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """class rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """class rectangle"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(' ', end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """class rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """class rectangle"""
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
        """class rectangle"""
        dic1 = {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
        return dic1
