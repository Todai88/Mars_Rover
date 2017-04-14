#!/usr/bin/env python3

"""

By: Joakim Bajoul Kakaei
For: ThoughtWorks

Reasoning:
The code might look a bit 'jumbled'; I might use one pattern or
coding style on one line and a different on another.
This is completely intentional as I wish to show that I can work
using different patterns.

It should also be mentioned that I don't have any extensive
experience with Python as I mainly work with VB.NET at work
and write JavaScript code at home / when I teach.

That being said I'm happy with my solution and I hope
you find it to your liking too.


"""

from rover import rover, directions
from mars import mars
import re


def validate_int(x, y):
    """
    Validate that the two parameters are integers.
    Re-used multiple times during the execution.
    """
    try:
        if int(x) >= 0 and int(y) >= 0:
            return True
    except ValueError as err:
        return False


def validate_rover(x, y, direction):
    """
    Validates a rover to ensure the parameters are
    correct datatypes(int, int, string).
    It also controls ensures that the integers
    are inside the Mars surface and that the
    supplied direction is a correct direction.
    """
    try:

        if validate_int(x, y) and direction in directions:
            return True
    except ValueError as err:
        return False

    return False

def validate_operations(op):
    """
    Uses regex to validate that
    the supplied string only contains
    'M', 'R' and 'L'.

    Raises a ValueError if incorrect
    operation(s) have been supplied.
    """
    pattern = re.compile("^[MRL]*$")

    if pattern.match(op):
        return True
    else:
        raise ValueError("Only values 'L', 'M' or 'R' accepted!")

def create_mars():
    while True:
        mars_object = None
        try:
            choice = input("Please enter the size of Mars (2 numbers, separated by a space and higher than 0.)\n>>> ").split()
            if len(choice) == 2 and validate_int(choice[0], choice[1]): # Checks so that the input is length 2 and then checks type-integrity
                mars_object = mars(int(choice[0]), int(choice[1]))
            else:
                print("Error: Please only enter two numerical values higher than 0 \
separated by a space!\n")
        except Exception as err:
            print(err)
            continue

        if mars_object is not None:
            return mars_object



def move(op, rover_object):
    """
    Uses the supplied operations
    and moves the rover according to
    the string of operations.

    If a rover goes out of bounds it is
    returned to its initial position
    (where it was initialized at).
    """
    try:
        for operation in op:
            if operation == "L":
                rover_object.turnLeft()
            elif operation == "R":
                rover_object.turnRight()
            else:
                rover_object.forward()
    except Exception as err:
        op = control_input(input("Error: {}\nReturning it to inital position ({}, {} facing {}).\
Try again!\n>>> ".format(err, rover_object.initial[0], rover_object.initial[1], rover_object.initial[2])))
        rover_object.return_to_start()
        move(op, rover_object)

def add_rover(mars_object):
    """
    Taking a reference to Mars
    this function asks for user input.
    The user input is then validate.
    If it passes validation a new Rover
    is created and returned.
    If the input doesn't pass validation
    the user is prompted to enter a
    new Rover.
    """
    while True:
        rover_object = None
        try:
            choice = control_input(input("Please enter the new Rover's initial position or enter 'exit' to end.\nRemember to keep inside Mars limits!\n>>> "), mars_object).split()
            if len(choice) == 3 and validate_rover(choice[0], choice[1], choice[2]):  # Check the length of supplied input and check type-integrity
                rover_object = rover(int(choice[0]), int(choice[1]), choice[2], mars_object)        # Initiate a rover with the supplied input. Each rover is assigned to a Mars (many-to-one relation).
                mars_object.occupied.append((int(choice[0]), int(choice[1]), choice[2])) # Add initial position to collection of Rovers.
            else:
                print("Error: You seem to have entered an incorrect Rover.\n\
Please only enter two numerical values greater than 0 and a character (N,E,S,W)\n")
        except (ValueError, RuntimeError) as err:
            print(err)
            continue

        if rover_object is not None:
            return rover_object

def move_rover(rover_object, mars_object):
    """
    Taking the created rover and mars
    the function then asks for user input.
    The input is validated and then
    sent to move() which then performs
    the operations.

    The Rover is then added to the
    occupied spaces on Mars and a
    new Rover will be prompted.
    """
    while True:
        moved = False
        try:
            choice = control_input(input("Enter a sequence of operations or enter 'exit' to end.\n>>> "), mars_object).upper()
            if validate_operations(choice): # Validate that the supplied operations are 'L', 'M' or 'R'
                mars_object.occupied = [item for item in mars_object.occupied if item != (rover_object.x, rover_object.y, rover_object.direction)]
                move(choice, rover_object)         # Peform the moves on the rover
                mars_object.occupied.append((rover_object.x, rover_object.y, rover_object.direction))
                moved = True
                print("\n--------------------------------------\n")
        except (RuntimeError, ValueError) as err:
            print(err)
            rover_object.return_to_start()
            continue

        if moved:
            return

def go_end(mars_object):
    """
    This function simply gives a pretty output
    of all the Rovers on Mars surface.
    Then exits the application.
    """
    print("--------------- Output ---------------")
    for rover_object in mars_object.occupied:
        print("{} {} {}".format(rover_object[0], rover_object[1], rover_object[2]))
    print("--------------------------------------")
    print("Exiting application.")
    exit()

def control_input(uinput, mars_object):
    if check_if_exit(uinput):
        go_end(mars_object)
    return uinput

def check_if_exit(iput):
    """
    Every input taken after setting up Mars will
    use this function to check if the input
    contains 'exit'.

    If it contains 'exit' it the go_end
    function will be called.
    """
    if "exit".upper() == iput.upper():
        return True
    return False

def main ():

    """
    The brains of the code.

    First invokes create_mars which sets up an object of mars.
    Then uses mars in a primitive form of dependency injection
    to set up a relationship (one mars to many rovers).

    Then initiates the entering of rovers and their operations.

    Main's main functions uses a few helper-functions, like
    validate_int, validate_rover, validate_operations etc to
    ensure correct data is inputted to the rover and the
    control centre.

    This validation is what I mention in the ReadMe-file, where
    I identify security and safety as the main concerns for
    this sort of an application.

    An "exit" when prompted will print the rover's positions.
    """

    mars_object = create_mars()
    print("\n-------------------------------------\n")
    while True:
            rover_object = add_rover(mars_object)
            move_rover(rover_object, mars_object)



if __name__ == "__main__":
    main()
