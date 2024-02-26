"""
Class will be the “base” of all other classes in this project
"""


class Base:
    """
    Class Base, private class attribute __nb_objects = 0
    if id is not None, assign the public instance
    attribute id with this argument value
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
