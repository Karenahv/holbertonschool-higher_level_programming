#!/usr/bin/python3
"""Unittests for Rectangle Class"""

import unittest
import json
import sys
from os import path, remove
import os
from io import StringIO
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.r1 = Rectangle(1, 2)
        self.r2 = Rectangle(5, 2)
        self.r3 = Rectangle(10, 3, 1, 0, 5)
        self.r4 = Rectangle(10, 3, 4, 0, 0)
        self.r5 = Rectangle(1, 1)
        self.r6 = Rectangle(2, 2)

    def tearDown(self):
        del self.r1
        del self.r2
        del self.r3
        del self.r4
        del self.r5
        del self.r6
        Base.__Base__nb_objects = 0

    def test_instance(self):
        x = self.r1.id
        self.assertEqual(self.r1.id, x)
        self.assertEqual(self.r4.id, 0)
        self.assertIsNot(self.r1, Base)
        self.assertIsInstance(self.r1, Base)
        self.assertNotEqual(self.r1.id, self.r2.id)
        self.assertEqual(self.r3.id, 5)
        with self.assertRaises(TypeError):
            r_mthan5 = Rectangle(5, 2, 3, 2, 1, 4)

    def test_attributesasignment(self):
        self.assertEqual(self.r3.width, 10)
        self.assertEqual(self.r3.height, 3)
        self.assertEqual(self.r3.x, 1)
        self.assertEqual(self.r3.y, 0)
        with self.assertRaises(TypeError):
            r = Rectangle(x=1, y=1)

    def test_private_cls(self):
        with self.assertRaises(AttributeError):
            print(self.r3.__nb_objects)

    def test_private_instance_atr(self):
        with self.assertRaises(AttributeError):
            print(self.r3.__width)
        with self.assertRaises(AttributeError):
            print(self.r3.__height)
        with self.assertRaises(AttributeError):
            print(self.r3.__x)
        with self.assertRaises(AttributeError):
            print(self.r3.__y)

    def test_public_instance_atr(self):
        test_id = Rectangle(10, 12, 1, 2, 6)
        test_id.id = 200

    def test_negativa_val(self):
        with self.assertRaises(ValueError):
            r_negative = Rectangle(-2, 3, 4, 5)
        with self.assertRaises(Exception) as e:
            Rectangle(-2, 3, 4, 5)
        self.assertTrue('width must be > 0' in str(e.exception))

        with self.assertRaises(ValueError):
            r_negative = Rectangle(2, -3, 4, 5)
        with self.assertRaises(Exception) as e:
            Rectangle(2, -3, 4, 5)
        self.assertTrue('height must be > 0' in str(e.exception))

        with self.assertRaises(ValueError):
            r_negative = Rectangle(2, 3, -4, 5)
        with self.assertRaises(Exception) as e:
            Rectangle(2, 3, -4, 5)
        self.assertTrue('x must be >= 0' in str(e.exception))

        with self.assertRaises(ValueError):
            r_negative = Rectangle(2, 3, 4, -5)
        with self.assertRaises(Exception) as e:
            Rectangle(2, 3, 4, -5)
        self.assertTrue('y must be >= 0' in str(e.exception))

    def test_otherinput(self):
        with self.assertRaises(Exception) as e:
            Rectangle("karen", 3, 4, 5)
        self.assertTrue('width must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(2, {2, 1}, 4, 5)
        self.assertTrue('height must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(2, 3, [1], 5)
        self.assertTrue('x must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(2, 3, 4, 5.1)
        self.assertTrue('y must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(float('-inf'), 2, 0, 0)
        self.assertTrue('width must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(float('NaN'), 2, 0, 0)
        self.assertTrue('width must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(4.5, 2, 0, 0)
        self.assertTrue('width must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(2, 2.0, 0, 0)
        self.assertTrue('height must be an integer' in str(e.exception))

    def test_num_atributos(self):
        with self.assertRaises(TypeError):
            r_uno = Rectangle(5)
        r_dos = Rectangle(5, 4)
        self.assertEqual(r_dos.width, 5)
        self.assertEqual(r_dos.height, 4)
        r_tres = Rectangle(5, 4, 3)
        self.assertEqual(r_tres.x, 3)
        self.assertEqual(r_tres.y, 0)
        r_cuatro = Rectangle(5, 4, 3, 1)
        self.assertEqual(r_cuatro.y, 1)

    def test_public_methos(self):
        self.r1.width = 10
        self.r1.height = 5
        self.r1.x = 2
        self.r1.y = 3
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 5)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 3)

    def test_area(self):
        x = Rectangle(3, 2)
        self.assertEqual(x.area(), 6)

    def test_print(self):
        r = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r.width = 3
        r.height = 5
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "\
###\n\
###\n\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(5, 6, 7, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()

    def test_str(self):
        new = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(new), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        new = Rectangle(4, 6, 2, 1, 12)
        new.update(89)
        self.assertEqual(str(new), "[Rectangle] (89) 2/1 - 4/6")
        new.update(89, 2)
        self.assertEqual(str(new), "[Rectangle] (89) 2/1 - 2/6")
        new.update(89, 2, 3)
        self.assertEqual(str(new), "[Rectangle] (89) 2/1 - 2/3")
        new.update(89, 2, 3, 4)
        self.assertEqual(str(new), "[Rectangle] (89) 4/1 - 2/3")
        new.update(89, 2, 3, 4, 6)
        self.assertEqual(str(new), "[Rectangle] (89) 4/6 - 2/3")

    def test_update_1(self):
        """test update #1"""
        new = Rectangle(1, 1, 1, 1, 50)

        new.update(height=2)
        self.assertEqual(str(new), "[Rectangle] (50) 1/1 - 1/2")

        new.update(width=8, x=7)
        self.assertEqual(str(new), "[Rectangle] (50) 7/1 - 8/2")

        new.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(new), "[Rectangle] (89) 3/1 - 2/2")

        new.update(8, width=5)
        self.assertEqual(str(new), "[Rectangle] (8) 3/1 - 5/2")

    def test_to_dictionary(self):
        with self.assertRaises(TypeError) as e:
            Rectangle.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)
        r = Rectangle(1, 2, 0, 0, 1)
        d = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)

    if __name__ == '__main__':
        unittest.main()
