#!/usr/bin/python3
"""
Class Student that defines a student
"""


class Student:
    """A class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dic = {}
        if attrs is not None:
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_dic[key] = value
            return my_dic
        return self.__dict__
