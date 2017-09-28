"""This file contains the functions to parse a string into a (binary) tree"""
from pythonds.basic.stack import Stack

from proof_machine.interaction.parser.infix_postfix import infix_to_postfix, postfix_to_infix
from proof_machine.object.namespace import lookup_ptype, lookup_state
from proof_machine.object.tree import BinaryTree, Node
from proof_machine.others import is_float


def parse(expr, namespace):
    """converts the input str into full infix notation then parses it into a tree"""
    postfix_expr = infix_to_postfix(expr, namespace)
    full_infix_expr = postfix_to_infix(postfix_expr, namespace)
    return build_parse_tree(full_infix_expr, namespace)


def build_parse_tree(fpexp, namespace):
    """parses a str in full infix notation into a tree"""
    token_list = fpexp.split()  # Expression to be parsed
    expr_tree = BinaryTree('')  # Expression Tree
    parent_stack = Stack()  # Keep track of the parent node
    parent_stack.push(expr_tree)

    current_tree = expr_tree
    for i in token_list:
        var_parse_type = lookup_ptype(i, namespace)
        if var_parse_type == 'undefined':
            # Add the symbol to global namespace if it's a numeric
            if is_float(i):
                namespace.defineVariable('symbol', i)
                var_parse_type = lookup_ptype(i, namespace)
        # Add nodes and move down/right the tree
        if var_parse_type == 'function':
            current_tree.key = Node(i, 'function', lookup_state(i, namespace))
            current_tree.insertLeft('')
            parent_stack.push(current_tree)
            current_tree = current_tree.leftChild
        elif var_parse_type == 'operator':
            current_tree.key = Node(i, 'operator', lookup_state(i, namespace))
            current_tree.insertRight('')
            parent_stack.push(current_tree)
            current_tree = current_tree.rightChild
        elif i in ['{', '[', '(']:
            current_tree.key = Node(i, 'parentheses', lookup_state(i, namespace))
            current_tree.insertLeft('')
            parent_stack.push(current_tree)
            current_tree = current_tree.leftChild
        # Add nodes and move up the tree
        elif var_parse_type == 'symbol':
            current_tree.key = Node(i, 'symbol', lookup_state(i, namespace))
            current_tree = parent_stack.pop()  # move up one level
            while current_tree.key.ptype == 'function' and not parent_stack.isEmpty():
                current_tree = parent_stack.pop()
        elif i in [')', ']', '}']:
            current_tree = parent_stack.pop()
            while current_tree.key.ptype == 'function' and not parent_stack.isEmpty():
                current_tree = parent_stack.pop()
        else:
            raise ValueError(
                "Variable " + i + " has wrong parse type: " + var_parse_type + \
                ". Must be 'function', 'operator', 'symbol' or 'parentheses'.")

    return expr_tree
