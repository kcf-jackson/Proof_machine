"""The file contains functions to infer states of a tree"""
from pythonds.basic.queue import Queue
from pythonds.basic.stack import Stack

from proof_machine.others import unique


def infer_state(tree):
    """infers state starting from the bottom of the tree"""
    res_stack = Stack()
    res_stack.push(tree)

    # populate stack to loop over later
    node_queue = Queue()
    enqueue_and_push_children(node_queue, res_stack, tree)
    while not node_queue.isEmpty():
        current = node_queue.dequeue()
        enqueue_and_push_children(node_queue, res_stack, current)

    # Now loop from the bottom of the tree and infer state
    while not res_stack.isEmpty():
        current = res_stack.pop()
        if current.key.ptype in ['function', 'operator']:
            left_state = current.left_child.key.state if current.left_child is not None else []
            right_state = current.right_child.key.state if current.right_child is not None else []
            new_state = merge_state(current.key.state, unique(left_state + right_state))
            current.key.state = new_state
    return tree


def enqueue_and_push_children(node_queue, res_stack, tree):
    """enqueues and pushes children if they are not empty"""
    left_child = tree.left_child
    right_child = tree.right_child
    if left_child is not None:
        node_queue.enqueue(left_child)
        res_stack.push(left_child)
    if right_child is not None:
        node_queue.enqueue(right_child)
        res_stack.push(right_child)


def merge_state(state_list, add_state_list):
    """merges two lists of states"""
    return unique(state_list + add_state_list)
