README

INTRODUCTION:

I've been faced with a coding challenge where I'm to develop
a system to handle a squad of Mars Rovers.

I would assume that this is created for and/or by NASA or another
space agency where security and safety are key. As such
I will keep that in mind during the development of both
tests and actual code.

- Evidence it works:

Running ./main.py:
https://asciinema.org/a/anp62vg2i80grcjqjuul9uivx

Running ./test_all.bash:
https://asciinema.org/a/a0fbwd5kj2f66qdzih25fbsw1

-------------------------------------------------------------------------------

HOW TO:

I solved the challenge by using Python3 on both a Windows (running CygWin) machine
as well as on an Ubuntu machine.

Simply start the program by running ./main.py
Nothing else to it.

Test cases will be in the same folder if you wish to run them.

I've also included a .bash file that will run all the test-cases and
print their results to the screen.

Run this with ./test_all.bash


If you get any sort of errors when running any of the code (you shouldn't!),
it might have to do with the #shebang in the top of the file.
Simply run a "which bash" and change the #shebang to the output of that command!

Except the unittests, bash-script and main.py the files won't work individually.

-------------------------------------------------------------------------------

FORMAL REQUIREMENTS:

To develop a program that simulates two primary objects; Mars(1) and Rover(N).
After a Rover has been created it will be fed a sequence of operators
which will in turn move the Rover from it's staring position.
When (and only after!) the previous Rover has been moved will another
Rover be allowed to be created.

- Workflow;

    1. Initiate Mars (like you would initiate any Board).
    2. Initiate a Rover with position (X > 0 < Mars.x, Y > 0 < Mars.y) and a
        direction ('N', 'E', 'S' or 'W').
    3. Send operations to Rover (only 'L', 'M' and 'R' allowed)
    4. Move Rover from initial position to where supplied operations will leave it.
    5. Go back to step 2 and repeat until "exit" has been typed.

    Upon "exit" the current position of the Rovers will be printed.

- Personal additions to the formal requirements:

Requirements document is missing any sort of UI/UX; I need to add
at least prompts to help user through the workflow.

No error-handling / validation is visible in the test cases.
For security/safety reasons that needs to be handled.
(We don't want a user to send incorrect, undefined operations to the Rover!)

Certain advanced test-cases are not considered:
What if a Rover gets initiated on another Rover? That would surely
not be considered good design when developing a security/safety-centric
application.
Another case would be if a Rover enters the space of another Rover
when moving. That would also not be considered good planning.

NOTICE that when a Rover has been supplied with VALID operations it will attempt
to move from its initial position to its end position (as defined by operations).
Unless it goes out of bounds or hits another Rover during its movement it will
move to its end position where it will stay until "exit" has been typed.
If it hits another Rover or goes out of bounds it will be returned to its
initial position and the user will be prompted to enter new operations.

What is important to note about that is that I made a conscious decision
to move a Rover immediately after getting its operations, instead of waiting
for all Rovers to have had their operations fed to them.
However, if that would be a formal requirement rather than an open ended
requirement (as per your specification), that could easily be changed
by manipulating a few lines of code.

-------------------------------------------------------------------------------

SOLUTION:

I started by writing up a basic UML class-diagram (note to self, scan and add
to compressed file).
On this class diagram I wrote up classes attributes, functions.
Then I created a basic flowchart to handle basic flow and state-handling.
After that I started writing some basic test-cases.
Finally I started coding to solve the test-cases I had set out for myself,
hoping that I wouldn't need to add more test-cases (of course I had to..) during development.

I made some assumptions along the way, most of which are outlined under
"Personal additions to the formal requirements" above.

But basically I tried to approach this as it was any other project I had to develop,
with the difference that this would be highly security- and safety-critical.
Rovers are highly expensive equipment (not to mention the cost of getting them to Mars),
so we need to make sure that we keep them intact.
So I started by asking myself the question "How do we keep the Rovers intact?",
we make sure they can't be on the same space as another Rover.
As any other rational person I then asked myself
"When can two Rovers possibly be on the same space?".
During initialisation and movement, at any other time the current Rover
and any previous Rovers will be stationary and cannot be moved again.

I've attempted to separate my concerns by using two different classes
over three different files.

    * main.py handles all user input and the flow of the application;
      it basically works as a delegator between the classes. it also
      covers most of the input validation.

    * mars.py is basically a board similar to what you would
      see in most games. It holds three values: x (int), y (int) and
      occupied (list). Occupied is simply a list of tuples holding
      the position and the direction a Rover is looking at.

    * rover.py is similar to a player you would see in most games.
      It holds 5 values: Mars (the mars it's assigned to), x (int),
      y (int), direction (char) and initial (a tuple with its initial position).
      It also has a few functions which handle movement and the validation
      of its position to ensure it doesn't hit another Rover or is out
      of bounds.

The reason I decided to split the code up in multiple files was to
make sure the code would be more easily testable and maintainable.
So each python file has its own test-file.
In the test-files you might notice a little comment next to all the
tests. I do that to make sure I have tested it successfully. Cute, huh? :3

Another question I asked myself was how to handle the user input. More
importantly how to finish the loop.
Looking at the test-cases we know that there is no formal requirement
as to how many Rovers to be handled at one execution.
So I decided to keep the application-state open
until the user types "exit" or "EXIT" any time after having
initialized Mars.

Of course all user input is validated, this could be to
check the type-integrity of input to checking if the input
corresponds to the correct RegEx (for operations).

One other important thing that I tried to keep in mind was to
use as many different patterns and data types as possible.
This was a conscious choice as I wanted to show that I can use
them. I'm sorry if it's messy, but I thought
it was important to show that there is a foundation that
can be built upon.
