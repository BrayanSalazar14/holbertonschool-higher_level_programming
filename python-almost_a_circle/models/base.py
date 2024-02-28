#!/usr/bin/python3
"""
Class will be the “base” of all other classes in this project
"""
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        class_name = str(cls.__name__) + ".json"
        if list_objs is not None:
            list_objs_list = [obj.to_dictionary() for obj in list_objs]
        with open(class_name, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        my_instance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        my_instance.update(**dictionary)
        return my_instance

    @classmethod
    def load_from_file(cls):
        class_name = str(cls.__name__) + ".json"
        if not os.path.exists(class_name):
            return []
        list_of_instances = []
        with open(class_name, "r", encoding="utf-8") as file:
            list_iterate = cls.from_json_string(file.read())
            list_of_instances = [cls.create(**obj) for obj in list_iterate]
        return list_of_instances
