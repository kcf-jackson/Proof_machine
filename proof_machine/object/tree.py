"""This file contains the BinaryTree class"""
from pythonds import Queue

from .node import is_node


class BinaryTree:
    """represents mathematical expressions.

    Attributes:
        key (Node), left_child (BinaryTree), right_child (BinaryTree)
    """

    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_obj):
        """ Insert a tree into the left_child. """
        tmp_tree = new_obj if is_binary_tree(new_obj) else BinaryTree(new_obj)
        if self.left_child is not None:
            tmp_tree.left_child = self.left_child
        self.left_child = tmp_tree

    def insert_right(self, new_obj):
        """ Insert a tree into the right_child. """
        tmp_tree = new_obj if is_binary_tree(new_obj) else BinaryTree(new_obj)
        if self.right_child is not None:
            tmp_tree.right_child = self.right_child
        self.right_child = tmp_tree

    # Output / Display functions
    def view(self, return_object=False):
        """ Print out the string representation of a tree """
        res = self.get_str()
        print(res)
        if return_object:
            return res

    def get_str(self):
        """ Converts a tree to string """
        current_node = self.key
        node_type = current_node.ptype
        node_symbol = str(current_node.value)
        if node_type == 'function':
            return node_symbol + ' ( ' + self.left_child.get_str() + ' ) '
        elif node_type == 'symbol':
            return node_symbol
        elif node_type == 'operator':
            return '( ' + self.left_child.get_str() + ' ' + node_symbol + ' ' + self.right_child.get_str() + ' )'
        elif node_type == 'parentheses':
            return '( ' + self.left_child.get_str() + ' )'

    def print_full_tree(self, level=0):
        """prints out the tree (by levels) """
        print("  " * level + self.key.value + ' ' + self.key.ptype)
        if self.left_child != None:
            self.left_child.print_full_tree(level + 1)
        if self.right_child != None:
            self.right_child.print_full_tree(level + 1)

    # Extract parts from tree
    def flatten(self, node_tree_indicator=None):
        """maps a tree into a list of nodes / subtrees with breadth-first order
        Args:
            node_tree_indicator(str): Node is 0, Tree is 1."""

        # By default it returns a list of nodes.
        if node_tree_indicator is None or node_tree_indicator == []:
            node_tree_indicator = '0' * self.count_num_nodes()

        res = [self.key] if node_tree_indicator[0] == '0' else [self]
        node_queue = Queue()
        node_queue = enqueue_children(self, node_queue)

        count = 1  # count must start at 1
        while not node_queue.isEmpty() and count < len(node_tree_indicator):
            current = node_queue.dequeue()
            if node_tree_indicator[count] == '0':
                res.append(current.key)
                node_queue = enqueue_children(current, node_queue)
            elif node_tree_indicator[count] == '1':
                res.append(current)
            count += 1
        return res

    def get_subtrees(self):
        """gets all sub-trees by looping over the tree and collecting trees that have at least one child."""
        node_queue = Queue()
        enqueue_children(self, node_queue)
        res = [self]
        while not node_queue.isEmpty():
            current_tree = node_queue.dequeue()
            node_queue = enqueue_children(current_tree, node_queue)
            if not current_tree.is_leaf():
                res.append(current_tree)
        return res

    def get_symbols(self):
        """converts a tree into list of symbols"""
        nodes_list = self.flatten()
        sym_list = [x.value for x in nodes_list]
        return sym_list

    # Auxiliary functions
    def relabel_nodes(self, node_list):
        """relabels the tree with a list of flatten in breadth-first order"""
        head, tail = node_list[0], node_list[1:]
        if is_binary_tree(head):
            return head
        self.key = head
        node_queue = Queue()
        node_queue = enqueue_children(self, node_queue)
        while len(tail) > 0:
            head, tail = tail[0], tail[1:]
            current_tree = node_queue.dequeue()
            if is_node(head):
                current_tree.key = head
                node_queue = enqueue_children(current_tree, node_queue)
            elif is_binary_tree(head):
                current_tree.key = head.key
                current_tree.left_child = head.left_child
                current_tree.right_child = head.right_child

    def count_num_nodes(self):
        """counts the number of flatten in a tree"""
        res = [self.key]
        node_queue = Queue()
        node_queue = enqueue_children(self, node_queue)
        while not node_queue.isEmpty():
            current_tree = node_queue.dequeue()
            res.append(current_tree.key)
            enqueue_children(current_tree, node_queue)
        return len(res)

    def is_leaf(self):
        """checks if a tree is a leaf (i.e. has no children). """
        return (not self.left_child) and (not self.right_child)


def is_binary_tree(obj):
    """checks if an object is a BinaryTree. """
    return isinstance(obj, BinaryTree)


def enqueue_children(tree, node_queue):
    """enqueues children (if they are not empty)"""
    left_child = tree.left_child
    right_child = tree.right_child
    if left_child is not None:
        node_queue.enqueue(left_child)
    if right_child is not None:
        node_queue.enqueue(right_child)
    return node_queue
