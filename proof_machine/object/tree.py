class Node:
    """represents mathematical symbols.

    Attributes:
        value (str): A text / mathematical symbol.

        ptype (str): One of 'symbol', 'function', 'parentheses' and 'operator'.

        state (list of str): List of mathematical properties.

        latex (str)
    """

    def __init__(self, value, ptype, state=['']):
        self.value = value
        self.ptype = ptype
        self.state = state

    def View(self):
        """ Print out all the attributes of the object. """
        print("Content: {}, Type: {}, State: {}".format(self.value, self.ptype, self.state))


def is_node(obj):
    """ Check if an object is a Node. """
    return isinstance(obj, Node)


class BinaryTree:
    """represents mathematical expressions.
    
    Attributes:
        key (Node), leftChild (BinaryTree), rightChild (BinaryTree)
    """

    def __init__(self, root_obj):
        self.key = root_obj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, new_obj):
        """ Insert a tree into the leftChild. """
        t = new_obj if is_binary_tree(new_obj) else BinaryTree(new_obj)
        if self.leftChild is not None:
            t.left = self.leftChild
        self.leftChild = t

    def insertRight(self, new_obj):
        """ Insert a tree into the rightChild. """
        t = new_obj if is_binary_tree(new_obj) else BinaryTree(new_obj)
        if self.rightChild is not None:
            t.right = self.rightChild
        self.rightChild = t

    def is_leaf(self):
        """ Check if a tree is a leaf (i.e. has no children). """
        return (not self.leftChild) and (not self.rightChild)

    # Output / Display functions
    def View(self, display=True):
        """ Print out the string representation of a tree """
        res = self.str()
        if display:
            print(res)
        return res

    def str(self):
        """ Convert a tree to string """
        current_node = self.key
        node_type = current_node.ptype
        node_symbol = str(current_node.value)
        if node_type == 'function':
            return node_symbol + ' ( ' + self.leftChild.str() + ' ) '
        elif node_type == 'symbol':
            return node_symbol
        elif node_type == 'operator':
            return '( ' + self.leftChild.str() + ' ' + node_symbol + ' ' + self.rightChild.str() + ' )'
        elif node_type == 'parentheses':
            return '( ' + self.leftChild.str() + ' )'

    def print_full_tree(self, level=0):
        """ Print out the tree (by levels) """
        print("  " * level + self.key.value + ' ' + self.key.ptype)
        if self.leftChild != None:
            self.leftChild.print_full_tree(level + 1)
        if self.rightChild != None:
            self.rightChild.print_full_tree(level + 1)


def is_binary_tree(obj):
    """ Check if an object is a BinaryTree. """
    return isinstance(obj, BinaryTree)
