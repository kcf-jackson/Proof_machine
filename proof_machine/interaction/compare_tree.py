"""This function contains functions to check equality between two trees."""
from proof_machine.others import which
from .encode_tree import tree_to_base_three_code


# Tree equality
# def treeEqualityByNodeValues(tree1, tree2):

# def treeEqualityByNodeTypes(tree1, tree2):

def tree_equality_by_structure(tree1, tree2):
    """checks if two trees has the same base-three code"""
    return tree_to_base_three_code(tree1) == tree_to_base_three_code(tree2)


def tree_diff(tree1, tree2):
    """computes a difference score between two trees"""
    count_dict1 = count_nodes(tree1)
    count_dict2 = count_nodes(tree2)
    diff = 0
    for item in count_dict1:
        if item in count_dict2:
            diff += abs(count_dict1[item] - count_dict2[item])
        else:
            diff += count_dict1[item]
    for item in count_dict2:
        if item not in count_dict1:
            diff += count_dict2[item]
    return diff


def count_nodes(tree1):
    """counts each symbol in a tree"""
    nodes_list = tree1.flatten()
    sym_list = [x.value for x in nodes_list]
    key = set(sym_list)
    count_dict = {}
    for k in key:
        count_dict[k] = sym_list.count(k)
    return count_dict


def tree_diff_list(tree, tree_list):
    """computes a list of difference scores from a tree"""
    return [tree_diff(tree, x) for x in tree_list]


def min_diff_tree(tree, tree_list):
    """finds the tree with the minimum difference in a list"""
    import random
    score_list = tree_diff_list(tree, tree_list)
    index = (which(score_list, min(score_list)))
    index = random.sample(index, 1)[0] if len(index) > 1 else index[0]
    return tree_list[index]
