#!/usr/bin/python3
""" tests for max_integer function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestStringMethods(unittest.TestCase):
    """ tests for max_integer function"""

    def test_fstpositive(self):
        """ tests for max_integer function"""
        list1 = [10, 9, 8, 7]
        self.assertEqual(max_integer(list1), 10)

    def test_lastpositive(self):
        """ tests for max_integer function"""
        list1 = [10, 9, 8, 30]
        self.assertEqual(max_integer(list1), 30)

    def test_positive(self):
        """ tests for max_integer function"""
        list1 = [10, 50, 8, 7]
        self.assertEqual(max_integer(list1), 50)

    def test_negative(self):
        """ tests for max_integer function"""
        list1 = [10, 9, -10, 7]
        self.assertEqual(max_integer(list1), 10)

    def test_allnegatives(self):
        """ tests for max_integer function"""
        list1 = [-1, -3, -4, -10]
        self.assertEqual(max_integer(list1), -1)

    def empty(self):
        """ tests for max_integer function"""
        list1 = []
        self.assertEqual(max_integer(list1), None)

    def test_oneelement(self):
        """ tests for max_integer function"""
        list1 = [9]
        self.assertEqual(max_integer(list1), 9)

if __name__ == '__main__':
    unittest.main()
