"""This file contains the Node class"""

from proof_machine.others import get_class


class Node:
    """represents mathematical symbols.

    Attributes:
        value (str): A text / mathematical symbol.

        ptype (str): One of 'symbol', 'function', 'parentheses' and 'operator'.

        state (list of str): List of mathematical properties.

        latex (str): corresponding latex syntax.
    """

    def __init__(self, value, ptype, state=None, latex=None):
        self.value = value
        self.ptype = ptype
        if state is not None and get_class(state) != 'list':
            raise ValueError("state must be of type 'list'.")
        self.state = state
        self.latex = value if latex is None else latex

    def view(self):
        """ Print out all the attributes of the object. """
        state_str = '' if self.state is None else ", ".join(self.state)
        latex_str = '' if self.latex is None else self.latex
        print("Content: {} \t Type: {:>12} \t State: {:>15} \t Latex: {}".format(
            self.value, self.ptype, state_str, latex_str))

    def modify(self, attr, new_value):
        """ Internal generic attributes setter """
        if attr not in ['value', 'ptype', 'state', 'latex']:
            raise ValueError(
                attr + " is not a valid attribute. It must be one of 'value', 'ptype', 'state' and 'latex'.")
        else:
            setattr(self, attr, new_value)


def is_node(obj):
    """ Check if an object is a Node. """
    return isinstance(obj, Node)
