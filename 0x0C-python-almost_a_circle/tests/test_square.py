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
        Base.__Base__nb_objects = 0
        self.s1 = Square(1)
        self.s2 = Square(5, 2)
        self.s3 = Square(10, 3, 1)
        self.s4 = Square(10, 3, 4, 0)

    def tearDown(self):
        del self.s1
        del self.s2
        del self.s3
        del self.s4
        Base.__Base__nb_objects = 0

    def test_instance(self):
        x = self.s1.id
        self.assertEqual(self.s1.id, x)
        self.assertEqual(self.s4.id, 0)
        self.assertIsNot(self.s1, Base)
        self.assertIsInstance(self.s1, Base)
        self.assertNotEqual(self.s1.id, self.s2.id)
        self.assertEqual(self.s3.id, 82)
        self.assertIsInstance(self.s1, Base)
        self.assertTrue(issubclass(type(self.s1), Rectangle), True)
        with self.assertRaises(TypeError):
            r_mthan4 = Square(5, 2, 3, 2, 1, 4)

    def test_attributesasignment(self):
        self.assertEqual(self.s3.size, 10)
        self.assertEqual(self.s3.x, 3)
        self.assertEqual(self.s3.y, 1)
        self.assertEqual(self.s4.size, 10)
        self.assertEqual(self.s4.x, 3)
        self.assertEqual(self.s4.y, 4)
        self.assertEqual(self.s3.id, 76)
        with self.assertRaises(TypeError):
            r = Rectangle(x=1, y=1)

    def test_private_cls(self):
        with self.assertRaises(AttributeError):
            print(self.s3.__nb_objects)

    def test_private_instance_atr(self):
        with self.assertRaises(AttributeError):
            print(self.s3.__size)
        with self.assertRaises(AttributeError):
            print(self.s3.__x)
        with self.assertRaises(AttributeError):
            print(self.s3.__y)

    def test_public_instance_atr(self):
        test_id = Square(10, 12, 1, 2)
        test_id.id = 200

    def test_different_val_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square("a")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([9, 3])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('-inf'))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square('NaN')
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.16)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("karen")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(size=0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(size=-10)

    def test_otherinput(self):
        with self.assertRaises(Exception) as e:
            Square("karen", 3, 4)
        self.assertTrue('width must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Square(2, {2, 1}, 4)
        self.assertTrue('x must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Square(2, 3, [1])
        self.assertTrue('y must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Square(2, 3, 4.1)
        self.assertTrue('y must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Square(float('-inf'), 2, 0, 0)
        self.assertTrue('width must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Square(float('NaN'), 2, 0, 0)
        self.assertTrue('width must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Square(4.5, 2, 0, 0)
        self.assertTrue('width must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Square(2, 2.0, 0, 0)
        self.assertTrue('x must be an integer' in str(e.exception))

    def test_num_atributos(self):
        with self.assertRaises(TypeError):
            s_empty = Square()
        s_dos = Square(5, 4)
        self.assertEqual(s_dos.width, 5)
        self.assertEqual(s_dos.x, 4)
        s_tres = Square(5, 4, 3)
        self.assertEqual(s_tres.y, 3)
        s_cuatro = Square(5, 4, 3, 1)
        self.assertEqual(s_cuatro.id, 1)

    def test_public_methos(self):
        self.s1.width = 10
        self.s1.x = 2
        self.s1.y = 3
        self.assertEqual(self.s1.width, 10)
        self.assertEqual(self.s1.x, 2)
        self.assertEqual(self.s1.y, 3)

    def test_area(self):
        x = Square(3)
        self.assertEqual(x.area(), 9)

    def test_str(self):
        news = Square(4, 6, 2, 1)
        self.assertEqual(str(news), "[Square] (1) 6/2 - 4")

    def test_update(self):
        news = Square(4, 6, 2, 1)
        news.update(89)
        self.assertEqual(str(news), "[Square] (89) 6/2 - 4")
        news.update(89, 2)
        self.assertEqual(str(news), "[Square] (89) 6/2 - 2")
        news.update(89, 2, 3)
        self.assertEqual(str(news), "[Square] (89) 3/2 - 2")
        news.update(89, 2, 3, 4)
        self.assertEqual(str(news), "[Square] (89) 3/4 - 2")

    def test_update_1(self):
        """test update #1"""
        new2 = Square(1, 1, 1, 50)

        new2.update(size=8, x=7)
        self.assertEqual(str(new2), "[Square] (50) 7/1 - 8")

        new2.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(new2), "[Square] (89) 3/1 - 2")

        new2.update(id=8, size=5)
        self.assertEqual(str(new2), "[Square] (8) 3/1 - 5")

    if __name__ == '__main__':
        unittest.main()
