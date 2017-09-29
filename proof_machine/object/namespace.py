from proof_machine.others import default_namespace, get_class


class Variable:
    """ represents mathematical symbols / variables.

    Attributes:
        name (get_str), state (list of get_str), latex (get_str), ptype (get_str): one of 'symbol', 'function', 'operator', 'parentheses'
    """

    def __init__(self, name, ptype='symbol', state=None, latex=None):
        self.name = name
        self.ptype = ptype
        if state is not None and get_class(state) != 'list':
            raise ValueError("state must be of type 'list'.")
        self.state = state
        self.latex = name if latex is None else latex

    def view(self):
        """ Print outs all the attributes of the object """
        state_str = '' if self.state == None else ", ".join(self.state)
        latex_str = '' if self.latex == None else self.latex
        print("{:>15} \t {:>12} \t {:>15} \t {:>12}".format(self.name, self.ptype, state_str, latex_str))

    # Internal generic attributes setter
    def modify(self, attr, new_value):
        """ Internal generic attributes setter """
        if attr not in ['name', 'ptype', 'state', 'latex']:
            raise ValueError(
                attr + " is not a valid attribute. It must be one of 'name', 'ptype', 'state' and 'latex'.")
        else:
            setattr(self, attr, new_value)


class Namespace:
    """ keeps track of all the mathematical variables defined.

    Attributes:
        variableList (list of Variable).
    """

    def __init__(self):
        self.variableList = []
        self.addDefault()

    # Variables related
    def addDefault(self):
        """ adds some commonly used variables. """
        self.defineVariable('parentheses', default_namespace()['parentheses'])
        self.defineVariable('operator', default_namespace()['arithmeticOperator'])
        self.defineVariable('operator', default_namespace()['setOperator'])

    def defineVariable(self, ptype, var_name, state=None, latex=None):
        """ defines new mathematical variable and adds to the variableList.

        Args:
            ptype (get_str), var_name (get_str or list of get_str), state (list of get_str), latex (get_str)

        Note:
            if var_name is a list, then state and latex variables are ignored.

        Examples:

                >>> import string

                >>> globalVariables = Namespace()

                Input a list for var_name:

                >>> globalVariables.defineVariable('symbol', list(string.ascii_lowercase) + list(string.ascii_uppercase))

                Usual usage for var_name:

                >>> globalVariables.defineVariable('symbol', 'X1', ['random variable'], 'X_1	')

                >>> globalVariables.view()
        """

        if var_name.__class__.__name__ == 'list':
            for var in var_name:
                self.addVariable(Variable(var, ptype, None, None))
        else:
            self.addVariable(Variable(var_name, ptype, state, latex))

    def findVariable(self, var_name):
        """ finds a variable by name and returns it if found """
        for x in self.variableList:
            if x.name == var_name:
                return x

    def addVariable(self, newVariable):
        """ adds a variable to the variableList"""
        if self.contains(newVariable.name):
            raise ValueError("Variable " + newVariable.name + " already exists.")
        else:
            self.variableList.append(newVariable)

    def modifyVariable(self, var_name, attr, new_value):
        """ [internal] modifies a variable's attribute """
        if not self.contains(var_name):
            raise ValueError("Cannot modify a variable that doesn't exist.")
        else:
            [var.modify(attr, new_value) for var in self.variableList if var.name == var_name]

    # State related
    def addState(self, var_name, new_value):
        """ adds a state to a variable in the variableList"""
        if not self.contains(var_name):
            raise ValueError("Cannot modify a variable that doesn't exist.")
        else:
            var = self.findVariable(var_name)
            if var:
                var.state = [new_value] if var.state is None else var.state + [new_value]

    def removeState(self, var_name, new_value):
        """ removes a state from a variable in the variableList"""
        if not self.contains(var_name):
            raise ValueError("Cannot modify a variable that doesn't exist.")
        else:
            var = self.findVariable(var_name)
            var.state.remove(new_value)

    def contains(self, var_name):
        """ checks if a variable exists (by name) """
        return any([x.name == var_name for x in self.variableList])

    def view(self):
        """ prints out each variable in the variableList. """
        print("{:>15} \t {:>12} \t {:>15} \t {:>12}".format("Variable", "Parse type", "State", "Latex"))
        [var.view() for var in self.variableList]


# Helper functions
def lookup_ptype(var_name, namespace):
    """ Helper function to look up the variable type in a given namespace """
    res = namespace.findVariable(var_name)
    return res.ptype if res else 'undefined'


def lookup_state(var_name, namespace):
    """ Helper function to look up the variable state in a given namespace """
    res = namespace.findVariable(var_name)
    return res.state if res else 'undefined'
