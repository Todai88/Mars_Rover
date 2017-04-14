#!/usr/bin/env python3

"""

rover_tests.py was finished a few hours before I started integrating
the Rover into the interface / delegator (main.py).

As always is the case some test-cases were added after the intial
draft of the document.

As this is the most exhaustive testing class I was considering
adding a setup and teardown on the mars object.

However I realized that it would make no sense as I might
have test cases that required a fresh board to work fine.

"""


from rover import rover
from mars import mars
import unittest

class TestRover(unittest.TestCase):

    def test_create_first_rover(self): #SUCCESS

        """
        Testing the first supplied rover_object
        """
        mars_object = mars(5, 5)
        rover_object = rover(1, 2, "N", mars_object)

        expected = (1, 2, "N")
        actual = rover_object.initial
        self.assertEqual(expected, actual, "AssertEqual failed: Tuples differ.")

        """
        Will now test if expected failed testcases will pass.
        """

        self.assertRaises(Exception, rover, 6, 1, "E", mars_object)
        self.assertRaises(Exception, rover, -1, 1, "E", mars_object)
        self.assertRaises(Exception, rover, 4, -1, "E", mars_object)
        self.assertRaises(Exception, rover, 5, 10, "E", mars_object)

    def test_create_second_rover(self):

        """
        Testing the first supplied rover_object
        """

        mars_object = mars(5, 5)
        rover_object = rover(3, 3, "E", mars_object)
        expected = (3, 3, "E")
        actual = rover_object.initial

        self.assertEqual(expected, actual, "Failed test")

    def test_create_rovers_out_of_bounds(self):
        """
        Will now test if expected failed testcases will pass.
        """
        mars_object = mars(5, 5)

        self.assertRaises(ValueError, rover, 6, 1, "E", mars_object)
        self.assertRaises(ValueError, rover, -1, 1, "E", mars_object)
        self.assertRaises(ValueError, rover, 4, -1, "E", mars_object)
        self.assertRaises(ValueError, rover, 5, 10, "E", mars_object)

    def test_create_incorrect_datatypes(self):
        """
        Will now test if exceptions are thrown when
        incorrect Rovers are created.
        """
        mars_object = mars(5, 5)

        self.assertRaises(ValueError, rover, "x", 1, "E", mars_object)
        self.assertRaises(ValueError, rover, -1, "y", "E", mars_object)
        self.assertRaises(ValueError, rover, 4, -1, "z", mars_object)

    def test_first_basic_case(self):
        """
        This unit test checks the first testcase supplied by you:
        Required user-input:
        5 5
        1 2 N
        LMLMLMLMM

        Should output:
        1 3 N

        In this use case the mars and rover objects are both
        initialized by the code and the movement corresponding
        to the operations will be performed.
        After each movement forward the position will be
        controlled by an assertEqual to ensure that
        the rover is on the correct position.
        """
        mars_object = mars(5, 5)
        rover_object = rover(1, 2, "N", mars_object)

        #
        # Perform the moves as defined by your testcase
        #

        rover_object.turnLeft()
        rover_object.forward()
        expected = "0 2 W"
        actual = rover_object.get_formatted_position()
        self.assertEqual(expected, actual, "Failed test")

        rover_object.turnLeft()
        rover_object.forward()
        expected = "0 1 S"
        actual = rover_object.get_formatted_position()
        self.assertEqual(expected, actual, "Failed test")

        rover_object.turnLeft()
        rover_object.forward()
        expected = "1 1 E"
        actual = rover_object.get_formatted_position()
        self.assertEqual(expected, actual, "Failed test")

        rover_object.turnLeft()
        rover_object.forward()
        expected = "1 2 N"
        actual = rover_object.get_formatted_position()
        self.assertEqual(expected, actual, "Failed test")

        rover_object.forward()
        expected = "1 3 N"
        actual = rover_object.get_formatted_position()
        self.assertEqual(expected, actual, "Failed test")

    def test_second_basic_test(self):
        """
        This unit test will check the second testcase supplied by you:
        Required user-input:
        5 5 (or on the same board, doesn't matter!)
        3 3 E
        MMRMMRMRRM

        Should output:
        5 1 E

        In this test case the mars and rover objects are both
        initialized by the code and the movement corresponding
        to the operations will be performed.
        After each movement forward the position will be
        controlled by an assertEqual to ensure that
        the rover is on the correct position.
        """

        mars_object = mars(5, 5)
        rover_object = rover(3, 3, "E", mars_object)

        #
        # Perform the moves as defined by your testcase
        #

        rover_object.forward()
        expected = "4 3 E"
        actual = rover_object.get_formatted_position()
        self.assertEqual(expected, actual, "Failed test")

        rover_object.forward()
        expected = "5 3 E"
        actual = rover_object.get_formatted_position()
        self.assertEqual(expected, actual, "Failed test")

        rover_object.turnRight()
        rover_object.forward()
        expected = "5 2 S"
        actual = rover_object.get_formatted_position()
        self.assertEqual(expected, actual, "Failed test")

        rover_object.forward()
        expected = "5 1 S"
        actual = rover_object.get_formatted_position()
        self.assertEqual(expected, actual, "Failed test")

        rover_object.turnRight()
        rover_object.forward()
        expected = "4 1 W"
        actual = rover_object.get_formatted_position()
        self.assertEqual(expected, actual, "Failed test")

        rover_object.turnRight()
        rover_object.turnRight()
        rover_object.forward()

        expected = "5 1 E"
        actual = rover_object.get_formatted_position()

        self.assertEqual(expected, actual, "Failed test")

        """
        Below I'll run some more advanced test cases
        where I'll be checking multiple Rovers on a
        Mars to check that it works fine.
        """

    def test_rover_on_rover(self):
        """
        Advanced test case to check if
        exception is raised when a Rover
        is initialized on top of another Rover.
        """

        mars_object = mars(10, 10)
        mars_object.occupied.append((5, 5, "N")) #Adding a rover_object to the occupied spaces.
        self.assertRaises(RuntimeError, rover, 5, 5, "S", mars_object) #Since the space is taken
                                                                #This test will give us a RuntimeError
        rover_object = rover(5, 4, "N", mars_object)
        self.assertRaises(RuntimeError, rover_object.forward) # Moving into a space already occupied by
                                                          # another Rover will also result in a RuntimeError

    def test_rover_collition(self):
        """
        Advanced test case to check if
        exception is raised when a Rover
        hits another Rover when moving.
        """

        mars_object = mars(10, 10)
        mars_object.occupied.append((4, 6, "E"))
        rover_object = rover(4, 4, "N", mars_object)
        expected = rover_object.get_current_position()
        rover_object.forward()

        self.assertRaises(RuntimeError, rover_object.forward)

    def test_return_to_start(self):
        """
        Building on advanced2 (above) I
        want to test the rover.return_to_start
        to ensure that a rover is at its initial
        position.
        """

        mars_object = mars(10, 10)
        rover_object = rover(4, 4, "N", mars_object)
        expected = rover_object.get_current_position()

        """ Moving Rover forward one step """
        rover_object.forward()

        """ Checking if current position is differnt from
            starting position """
        self.assertNotEqual(expected, rover_object.get_current_position(),
                            "On the same position")

        """ Finally to the bread and butter of the test; to check
            if the starting position is the same as the position
            our Rover is in after invoking return_to_start() """

        rover_object.return_to_start()
        self.assertEqual(expected, rover_object.get_current_position(),
                            "Not on the same position..")
if __name__ == '__main__':
    unittest.main(verbosity=2)
