#!/usr/bin/python3
"""Unittests for Base Class"""


import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def setUp(self):
        """ create instances of Base"""
        Base._Base__nb_objects = 0
        self.b1 = Base()
        self.b2 = Base(12)
        self.b3 = Base(None)
        self.b4 = Base(0)
        self.b5 = Base(-5)
        self.b6 = Base(2)
        self.b7 = Base(4)

    def teardown(self):
        """del instances of Base"""
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5
        del self.b6
        del self.b7
        Base.__Base__nb_objects = 0

    def test_instance(self):
        """ test instantiation"""

        # test with no argument id
        self.assertIsInstance(self.b1, Base)
        self.assertEqual(self.b1.id, 1)

        # test with positive argument id
        self.assertIsInstance(self.b2, Base)
        self.assertEqual(self.b2.id, 12)

        # test with None argument
        self.assertEqual(self.b3.id, 2)

        # test with zero id
        self.assertEqual(self.b4.id, 0)

        # test with negative id
        self.assertEqual(self.b5.id, -5)

    def test_to_json_string15(self):
        json_s = Base.to_json_string([{'width: 2'}, {'height': 3}])
        self.assertEqual(json_s, '[{"width": 2}, {"height": 3}]')
        self.assertEqual(type(json_s), str)
        self.assertEqual(type(None), '[]')
        self.assertEqual(type([]), '[]')

    def test_save_to_file16(self):
        import os
        # Square
        Base._Base__nb_objects = 0
        contenido2 = []
        s100 = (3, 2, 8)
        s200 = (5)
        Rectangle.save_to_file([s100, s200])
        with open("Square.json", encoding="utf-8") as Myfile:
            contenido2 = Myfile.read()
        contenido2_dict = json.loads(contenido2)
        j2_string = [{"y": 8, "x": 2, "id": 1, "size": 3},
                     {"y": 0, "x": 0, "id": 2, "size": 5}]
        self.assertEqual(contenido2_dict, j2_string)

        #None
        Base._Base__nb_objects = 0
        contenido3 = []
        Rectangle.save_to_file(None)
        with open("Square.json", encoding="utf-8") as Myfile2:
            contenido3 = Myfile2.read()
        contenido3_dict = json.loads(contenido3)
        j3_string = []
        self.assertEqual(contenido3_dict, j3_string)

        #empty
        Base._Base__nb_objects = 0
        contenido4 = []
        Rectangle.save_to_file("")
        with open("Square.json", encoding="utf-8") as Myfile3:
            contenido4 = Myfile3.read()
        contenido4_dict = json.loads(contenido4)
        j4_string = []
        self.assertEqual(contenido4_dict, j4_string)

    def test_from_json_string17(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = json.dumps(list_input)
        list_output = json.loads(json_list_input)
        self.assertEqual(list_output, list_input)
        self.assertEqual(type(list_output), list)
        self.assertEqual(type(list_output[0]), dict)
        self.assertEqual(type(list_output[0]), str)

        #Empty or none argument
        list1 = []
        self.assertEqual(list1, Base.from_json_string(None))
        self.assertEqual(list1, Base.from_json_string(""))

    def test_create18(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)

        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 == s2)
        self.assertFalse(s1 is s2)

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file = (list_rectangles_input)
        list_out = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_input[0]),
                         str(list_out[0]))
        self.assertEqual(str(list_rectangles_input[1]),
                         str(list_out[1]))

        s1 = Rectangle(10, 7, 2, 8)
        s2 = Rectangle(2, 4)
        list_squares_input = [r1, r2]
        Square.save_to_file = (list_squares_input)
        list_out = Square.load_from_file()
        self.assertEqual(str(list_squares_input[0]), str(list_out[0]))
        self.assertEqual(str(list_squares_input[1]), str(list_out[1]))

    if __name__ == '__main__':
        unittest.main()
