#!/usr/bin/python3
"""
Module class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square

    Args:
        Rectangle (Class Parent)
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        attributes = ['id', 'size', 'x', 'y']
        if args is not None and args != ():
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        dict_square = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return dict_square
