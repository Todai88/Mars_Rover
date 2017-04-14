"""
The Mars class is as simple as an object / class comes.

It gets initialized and has nothing but its own attributes.

The x and y are simply the upper-right border.
Occupied is a list of tuples(int, int, char) to simulate
Rover positions. It seemed more portable and less intrusive than
saving an entire Rover in the list.

"""
class mars(object):
    """
    As mentions above, creates a Mars-object.
    """
    def __init__(self, x, y):
        """
        Initializes a Mars-object.
        """
        self.x = x
        self.y = y
        self.occupied = []
