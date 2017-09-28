"""This file contains the Node class"""


class Node:
    """represents mathematical symbols.

    Attributes:
        value (str): A text / mathematical symbol.

        ptype (str): One of 'symbol', 'function', 'parentheses' and 'operator'.

        state (list of str): List of mathematical properties.

        latex (str)
    """

    def __init__(self, value, ptype, state=None):
        self.value = value
        self.ptype = ptype
        if state is not None:
            self.state = state

    def view(self):
        """ Print out all the attributes of the object. """
        print("Content: {}, Type: {}, State: {}".format(self.value, self.ptype, self.state))


def is_node(obj):
    """ Check if an object is a Node. """
    return isinstance(obj, Node)
