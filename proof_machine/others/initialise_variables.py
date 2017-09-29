import string


def default_namespace():
    """ Creates a default (name-)space of mathematical variables.

    Attributes:
        Symbols: alphaNumeric, greekAlphabet

        Functions: trigonometricFunction, hyperbolicFunction, elementaryFunction, setFunction, integrationFunction,
        probabilityFunction, arithmeticFunction, vectorSpaceFunction

        Operators: arithmeticOperator, logicOperator, setOperator, otherOperator

        Parentheses: parentheses
    """
    return dict(alphaNumeric=list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase),
                greekAlphabet=['alpha', 'beta', 'chi', 'delta', 'digamma', 'epsilon', 'eta', 'gamma', 'iota', 'kappa',
                               'lambda', 'mu', 'nu', 'omega',
                               'phi', 'pi', 'psi', 'rho', 'sigma', 'tau', 'theta', 'upsilon', 'varepsilon', 'varkappa',
                               'varphi', 'varpi', 'varrho', 'varsigma',
                               'vartheta', 'xi', 'zeta', 'Delta', 'Gamma', 'Lambda', 'Omega', 'Phi', 'Pi', 'Psi',
                               'Sigma',
                               'Theta', 'Upsilon', 'Xi', 'mho', 'nabla'],
                trigonometricFunction=['sin', 'cos', 'tan', 'sec', 'csc', 'cot', 'arcsin', 'arccos', 'arctan', 'arcsec',
                                       'arccsc', 'arccot'],
                hyperbolicFunction=['sinh', 'cosh', 'tanh', 'sech', 'csch', 'coth', 'arsinh', 'arcosh', 'artanh',
                                    'arsech',
                                    'arcsch', 'arcoth'], elementaryFunction=['exp', 'log', 'abs', 'sqrt', 'max', 'min'],
                setFunction=['I', 'sup', 'inf', 'limsup', 'liminf', 'cap_i', 'cup_i', 'cplm'],
                integrationFunction=['int', 'D'], probabilityFunction=['E', 'P'],
                arithmeticFunction=['sum_i', 'prod_i'], vectorSpaceFunction=['norm'],
                arithmeticOperator=['+', '-', '*', '/', '^', '<', '>', '<=', '>=', '='],
                logicOperator=['=>', '<=>', 'land', 'lor'], setOperator=['cup', 'cap', 'setDiff', 'symSetDiff'],
                otherOperator=['|', ','], parentheses=['{', '[', '(', ')', ']', '}'])


def get_precedence_table():
    """ Creates a precedence lookup table (dictionary). """
    return {
        "^": 4, "*": 3, "/": 3, "+": 2, "-": 2, '<': 1, '>': 1, '<=': 1, '>=': 1, '=': 1,
        "cap": 3, "cup": 2, "setDiff": 2, "symSetDiff": 2,
        "land": 3, "lor": 2,
        "(": 0, '|': 1, ',': 1
    }
