#!/usr/bin/env python3

"""

mars_test.py was by far the simplest to test as it
doesn't really have a lot of meat on its implementation.

Everything is super self-explanatory...
I simply test the upper-right limit on each of the
mars objects that have been initiated to an expected value.
"""

from mars import mars
import unittest

class TestMars(unittest.TestCase):

    def test_first_mars_init(self): #SUCCESS
        expected = [5, 5]
        mars_object = mars(5, 5)
        actual = [mars_object.x, mars_object.y]
        self.assertEqual(expected, actual, "Failed test")

    def test_second_mars_init(self): #SUCCESS
        expected = [10, 10]
        mars_object = mars(10, 10)
        actual = [mars_object.x, mars_object.y]
        self.assertEqual(expected, actual, "Failed test")

    def test_third_mars_init(self): #SUCCESS
        expected = [200, 200]
        mars_object = mars(200, 200)
        actual = [mars_object.x, mars_object.y]
        self.assertEqual(expected, actual, "Failed test")
if __name__ == "__main__":
    unittest.main(verbosity=2)
