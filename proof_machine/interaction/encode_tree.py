"""This file deals with the different encodings of a tree: LR code, base-3 code, leaves code."""
from pythonds.basic.queue import Queue

from proof_machine.object import BinaryTree, Node
from proof_machine.others import map2, unique


# Conversion between LR/baseThreeCode
# - Convert LR code to baseThreeCode
def lr_code_to_base_three_code(lr_code):
    """Converts LR code to baseThreeCode"""
    if len(lr_code) == 0:
        return '0'
    paths = [x for x in lr_code.split('0') if x != '']
    max_path_length = max([len(p) for p in paths])
    children = ['L', 'R']
    res = ""
    for i in range(max_path_length + 1):
        head = unique([x[:(i + 1)] for x in paths])
        new_complete_path, head = [x for x in head if len(x) == i], [x for x in head if len(x) >= (i + 1)]
        if len(new_complete_path) > 0:
            res += '0' * len(new_complete_path)
        for ind, _ in enumerate(children):
            if ind % 2 == 1:
                has_children = [x in head for x in children[(ind - 1):(ind + 1)]]
                num_children = sum(has_children)
                if num_children != 0:
                    res += str(num_children)
        children = sum([[x + 'L', x + 'R'] for x in children], [])
    return res


# - Convert baseThreeCode to LR code
def base_three_code_to_lr_code(base_three_code):
    """Converts base_three_code to LR code"""
    i, base_three_code = base_three_code[0], base_three_code[1:]
    if i in ['0', '1', '2']:
        path = ['L', 'R'][:int(i)]
    else:
        raise ValueError("The following character is not allowed: " + i + ", use only one of '0', '1', '2'.")
    completed_path = []
    while path != [] and base_three_code != '':
        num_open_path = count_open_path(path)
        i, base_three_code = base_three_code[:num_open_path], base_three_code[num_open_path:]
        all_paths = map2(path, i, add_lr_string)
        completed_path.append([x for x in all_paths if is_ended_path(x)])
        path = [x for x in all_paths if not is_ended_path(x)]
    return "".join(sum(completed_path, []))


# Build tree
# - Build tree from LR code
def lr_code_to_tree(lr_code):
    """Builds tree from LR code"""
    master_tree = BinaryTree(Node('root', 'symbol'))
    working_tree = master_tree
    for i in lr_code:
        if i == '0':
            working_tree = master_tree
        elif i == 'L':
            if working_tree.left_child is None:
                working_tree.insert_left(Node('L', 'symbol'))
            working_tree = working_tree.left_child
        elif i == 'R':
            if working_tree.right_child is None:
                working_tree.insert_right(Node('R', 'symbol'))
            working_tree = working_tree.right_child
        else:
            print("Character " + i + " is not allowed.")
    return master_tree


# - Build from baseThree(B3) code
def base_three_code_to_tree(base_tree_code):
    """Builds tree from baseThree(B3) code"""
    return lr_code_to_tree(base_three_code_to_lr_code(base_tree_code))


# Conversion from trees to codes
# - Convert tree to baseThree code
def tree_to_base_three_code(tree):
    """Converts tree to baseThree code"""
    node_queue = Queue()
    node_queue, num_children = count_children_and_enqueue(tree, node_queue)
    res = [str(num_children)]
    while not node_queue.isEmpty():
        current = node_queue.dequeue()
        node_queue, num_children = count_children_and_enqueue(current, node_queue)
        res.append(str(num_children))
    return "".join(res)


# - Convert tree to leaves indicator
def tree_to_leaves_indicator(tree):
    """Converts tree to leaves indicators (str) (Leaves are 1, others are 0)"""
    res = ""
    for num_children in tree_to_base_three_code(tree):
        res += '1' if num_children == '0' else '0'
    return res


def count_children_and_enqueue(tree, node_queue):
    """enqueues children if they are not empty"""
    num_children = 0
    left_child = tree.left_child
    right_child = tree.right_child
    if left_child is not None:
        num_children += 1
        node_queue.enqueue(tree.left_child)
    if right_child is not None:
        num_children += 1
        node_queue.enqueue(tree.right_child)
    return node_queue, num_children


# Helper functions
def is_ended_path(str0):
    """checks if the path has ended"""
    return str0[-1] == '0'


def count_open_path(list0):
    """counts the number of open paths"""
    return len(list0) - sum([is_ended_path(l) for l in list0])


def add_lr_string(str0, i):
    """expands a path according to the number of children it has"""
    i = str(i)
    local_dict = {'0': [str0 + '0'], '1': [str0 + 'L'], '2': [str0 + 'L', str0 + 'R']}
    if i in ['0', '1', '2']:
        return local_dict[i]
    else:
        raise ValueError("Error occurs in add_lr_string, input was " + str0 + ", " + i)
