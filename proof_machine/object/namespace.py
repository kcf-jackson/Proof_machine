"""This file contains the Namespace class."""
from proof_machine.others import default_namespace
from .node import Node


class Namespace:
    """ keeps track of all the mathematical variables defined.

    Attributes:
        variable_list (list of Variable).
    """

    def __init__(self):
        self.variable_list = []
        self.add_default()

    # Variables related
    def add_default(self):
        """ adds some commonly used variables. """
        self.define_variable('parentheses', default_namespace()['parentheses'])
        self.define_variable('operator', default_namespace()['arithmeticOperator'])
        self.define_variable('operator', default_namespace()['setOperator'])

    def define_variable(self, ptype, var_name, state=None, latex=None):
        """ defines new mathematical variable and adds to the variable_list.

        Args:
            ptype (str), var_name (str or list of str), state (list of str), latex (str)

        Note:
            if var_name is a list, then state and latex variables are ignored.

        Examples:

                >>> import string

                >>> globalVariables = Namespace()

                Input a list for var_name:

                >>> globalVariables.define_variable('symbol', list(string.ascii_lowercase) + list(string.ascii_uppercase))

                Usual usage for var_name:

                >>> globalVariables.define_variable('symbol', 'X1', ['random variable'], 'X_1	')

                >>> globalVariables.view()
        """

        if var_name.__class__.__name__ == 'list':
            for var in var_name:
                self.add_variable(Node(var, ptype, None, None))
        else:
            self.add_variable(Node(var_name, ptype, state, latex))

    def find_variable(self, var_name):
        """ finds a variable by name and returns it if found """
        for var in self.variable_list:
            if var.name == var_name:
                return var

    def add_variable(self, new_variable):
        """ adds a variable to the variable_list"""
        if self.contains(new_variable.name):
            raise ValueError("Variable " + new_variable.name + " already exists.")
        else:
            self.variable_list.append(new_variable)

    def modify_variable(self, var_name, attr, new_value):
        """ [internal] modifies a variable's attribute """
        if not self.contains(var_name):
            raise ValueError("Cannot modify a variable that doesn't exist.")
        else:
            _ = [var.modify(attr, new_value) for var in self.variable_list if var.name == var_name]

    # State related
    def add_state(self, var_name, new_value):
        """ adds a state to a variable in the variable_list"""
        if not self.contains(var_name):
            raise ValueError("Cannot modify a variable that doesn't exist.")
        else:
            var = self.find_variable(var_name)
            if var:
                var.state = [new_value] if var.state is None else var.state + [new_value]

    def remove_state(self, var_name, new_value):
        """ removes a state from a variable in the variable_list"""
        if not self.contains(var_name):
            raise ValueError("Cannot modify a variable that doesn't exist.")
        else:
            var = self.find_variable(var_name)
            var.state.remove(new_value)

    def contains(self, var_name):
        """ checks if a variable exists (by name) """
        return any([x.name == var_name for x in self.variable_list])

    def view(self):
        """ prints out each variable in the variable_list. """
        print("{:>15} \t {:>12} \t {:>15} \t {:>12}".format("Variable", "Parse type", "State", "Latex"))
        _ = [var.view() for var in self.variable_list]


# Helper functions
def lookup_ptype(var_name, namespace):
    """looks up a variable's ptype in a given namespace """
    res = namespace.find_variable(var_name)
    return res.ptype if res else 'undefined'


def lookup_state(var_name, namespace):
    """looks up a variable's state in a given namespace """
    res = namespace.find_variable(var_name)
    return res.state if res else 'undefined'


def get_node_from_namespace(var_name, namespace):
    """retrieves a variable from a given namespace """
    res = namespace.find_variable(var_name)
    return res if res else 'undefined'
