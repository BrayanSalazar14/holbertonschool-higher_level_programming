#!/usr/bin/python3
import json
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_init(self):
        Base._Base__nb_objects = 0

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(100)
        self.assertEqual(b3.id, 100)

        b4 = Base(-7)
        self.assertEqual(b4.id, -7)

    def test_to_json_string(self):
        Base._Base__nb_objects = 0

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(
            [{"id": 1, "name": "Alice"}]), '[{"id": 1, "name": "Alice"}]')

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertEqual(os.path.exists("Rectangle.json"), True)

        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        Square.save_to_file([s1, s2])
        self.assertEqual(os.path.exists("Square.json"), True)

    def test_from_json_string(self):
        Base._Base__nb_objects = 0

        dic1 = {"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}
        dict2 = {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}
        python_test_list = [dic1, dict2]
        json_to_string = Rectangle.to_json_string(python_test_list)
        list_output = Rectangle.from_json_string(json_to_string)
        self.assertEqual(list_output, python_test_list)

    def test_create(self):
        Base._Base__nb_objects = 0

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

        s1 = Square(4)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())

    def testModuleDoc(self):
        self.assertTrue(base.__doc__)

    def testClassDoc(self):
        self.assertTrue(Base.__doc__)


if __name__ == '__main__':
    unittest.main()
