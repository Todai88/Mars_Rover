#!/usr/bin/env python3

"""

main_test.py was the first of the unittests to be finished.

The tests are quite self-explanatory as they are really
easy to understand.

The main concerns are:
    * validate_int:
        - Takes two paramters and checks if they are integers >= 0
    * validate_rover:
        - Takes three parameters, uses validate_int to check the
          two first and then checks the second on the directions
          list in rover.py
    * validate_operations:
        - Takes a string of operations and checks if they only
          contain occurences of 'L' 'M' and 'R'.
"""


from main import validate_int, validate_operations, validate_rover, check_if_exit
import unittest

class TestMain(unittest.TestCase):

    def test_validate_int_correct(self): #SUCCESS
        self.assertTrue(validate_int(5, 3))

    def test_validate_int_with_strings(self): #SUCCESS
        self.assertFalse(validate_int("x", "y"))

    def test_validate_int_with_incorrect_integers_one(self): #SUCCESS
        self.assertFalse(validate_int(-1, 0))

    def test_validate_int_with_incorrect_integers_two(self): #SUCCESS
        self.assertFalse(validate_int(2, -1))

    def test_validate_rover_correct(self): #SUCCESS
        self.assertTrue(validate_rover(5, 3, "S"))

    def test_validate_rover_incorrect_number_x(self): #SUCCESS
        self.assertFalse(validate_rover(-1, 3, "E"))

    def test_validate_rover_incorrect_number_y(self): #SUCCESS
        self.assertFalse(validate_rover(4, -1, "N"))

    def test_validate_rover_incorrect_string(self): #SUCCESS
        self.assertFalse(validate_rover(3, 3, "X"))

    def test_validate_operations_supplied_test_case_one(self): #SUCCESS
        self.assertTrue(validate_operations("LMLMLMLMM"))

    def test_validate_operations_supplied_test_case_two(self): #SUCCESS
        self.assertTrue(validate_operations("MMRMMRMRRM"))

    def test_validate_operations_long_test(self): #SUCCESS
        self.assertTrue(validate_operations("\
MMRMMRMRRMMMRMMRMRRMMMRMMRMRRMMMRMMRMRRMMMRMMRMRRM\
MMRMMRMRRMMMRMMRMRRMMMRMMRMRRMMMRMMRMRRMMMRMMRMRRM\
MMRMMRMRRMMMRMMRMRRMMMRMMRMRRMMMRMMRMRRMMMRMMRMRRM\
"))

    def test_validate_operations_incorrect_start(self): #SUCCESS
        self.assertRaises(ValueError, validate_operations, "XLMR")

    def test_validate_operations_incorrect_middle(self): #SUCCESS
        self.assertRaises(ValueError, validate_operations,"LMXRL")

    def test_validate_operations_incorrect_end(self): #SUCCESS
        self.assertRaises(ValueError, validate_operations,"LMRX")

    def test_check_if_exit_correct_upper(self):
        self.assertTrue(check_if_exit("EXIT"))

    def test_check_if_exit_correct_lower(self):
        self.assertTrue(check_if_exit("exit"))

    def test_check_if_exit_not_exit(self):
        self.assertFalse(check_if_exit("notexit"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
