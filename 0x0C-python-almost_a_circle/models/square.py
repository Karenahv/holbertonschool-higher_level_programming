#!/usr/bin/python3
""" class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ class Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ class Square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

    @property
    def size(self):
        """ class Square"""
        return self.width

    @size.setter
    def size(self, value):
        """ class Square"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ class Square"""
        lenofargs = len(args)
        if lenofargs > 0:
            self.id = args[0]
            lenofargs -= 1
        if lenofargs > 0:
            self.size = args[1]
            lenofargs -= 1
        if lenofargs > 0:
            self.x = args[2]
            lenofargs -= 1
        if lenofargs > 0:
            self.y = args[3]
        if kwargs:
            for key, value in kwargs.items():
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'size':
                    self.width = value
                if key == 'id':
                    self.id = value

    def to_dictionary(self):
        """ class Square"""
        dic2 = {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
        return dic2
