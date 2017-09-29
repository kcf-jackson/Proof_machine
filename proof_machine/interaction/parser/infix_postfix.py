"""The file contains functions to convert between the different notations (infix, postfix, postfix simplified)"""
from pythonds.basic.stack import Stack

from proof_machine.object import lookup_ptype
from proof_machine.others import get_precedence_table


def infix_to_postfix(expr, namespace):
    """ Convert string in infix notation to postfix notation """
    precedence_table = get_precedence_table()
    op_stack = Stack()
    postfix_list = []

    token_list = expr.split()
    for token in token_list:
        # symbol
        token_ptype = lookup_ptype(token, namespace)
        if token_ptype == 'symbol':
            postfix_list.append(token)
        # parentheses or functions
        elif token == '(' or token_ptype == 'function':
            op_stack.push(token)
            if token not in precedence_table:
                precedence_table[token] = 0
        elif token == ')':
            top_token = op_stack.pop()
            # pop untils you see a open parentheses
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
            if not op_stack.isEmpty() and lookup_ptype(op_stack.peek(), namespace) == 'function':
                top_token = op_stack.pop()
                postfix_list.append(top_token)
        # operator
        elif token == 'operator':
            while not op_stack.isEmpty() and precedence_table[op_stack.peek()] >= precedence_table[token]:
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
        else:
            raise ValueError("This token" + token + "is not one of 'symbol', 'function', parentheses' or 'operator'.")

    while not op_stack.isEmpty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


def postfix_to_infix(expr, namespace):
    """ Convert string in postfix notation to infix notation """
    symbol_stack = Stack()
    token_list = expr.split()

    for token in token_list:
        token_ptype = lookup_ptype(token, namespace)
        if token_ptype == 'symbol':
            symbol_stack.push(token)
        elif token_ptype == 'operator':
            right = symbol_stack.pop()
            left = symbol_stack.pop()
            symbol_stack.push(" ".join(['(', left, token, right, ')']))
        elif token_ptype == 'function':
            center = symbol_stack.pop()
            # symbol_stack.push(" ".join([token, '(', center, ')']))
            symbol_stack.push(" ".join([token, center]))
        else:
            raise ValueError(token + " has the wrong parse type.")

    if symbol_stack.size() == 1:
        return symbol_stack.pop()
    else:
        raise ValueError("Final outcome doesn't have size 1.")


def postfix_to_infix_simplified(expr, namespace):
    """converts string in postfix notation into infix simplified notation"""
    precedence_table = get_precedence_table()  # need this to know what can be simplified
    symbol_stack = Stack()
    precedence_stack = Stack()
    token_list = expr.split()

    for token in token_list:
        token_ptype = lookup_ptype(token, namespace)
        if token_ptype == 'symbol':
            symbol_stack.push(token)
            precedence_stack.push(100)
        elif token_ptype == 'operator':
            right = symbol_stack.pop()
            left = symbol_stack.pop()

            token_prec = precedence_table[token]
            right_prec = precedence_stack.pop()
            left_prec = precedence_stack.pop()
            if left_prec < token_prec:
                left = '( ' + left + ' )'
            if right_prec <= token_prec:
                right = '( ' + right + ' )'
            precedence_stack.push(precedence_table[token])

            symbol_stack.push(" ".join([left, token, right]))
        elif token_ptype == 'function':
            if token not in precedence_table:
                precedence_table[token] = 0
            precedence_stack.pop()
            precedence_stack.push(100)
            center = symbol_stack.pop()
            symbol_stack.push(" ".join([token, '(', center, ')']))
        else:
            raise ValueError(token + " has the wrong parse type.")

    if symbol_stack.size() == 1:
        return symbol_stack.pop()
    else:
        raise ValueError("Final outcome doesn't have size 1.")


def tidy_view(tree, namespace, return_object=False):
    """takes a tree and prints out a string in simplified infix notation"""
    postfix = infix_to_postfix(tree.get_str(), namespace)
    print(postfix_to_infix_simplified(postfix, namespace))
    if return_object:
        return postfix_to_infix_simplified(postfix, namespace)
