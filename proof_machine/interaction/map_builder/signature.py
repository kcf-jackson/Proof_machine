""" This file contains the functions to handle the signature of a map / tree"""
from proof_machine.interaction.encode_tree import tree_to_leaves_indicator
from proof_machine.object import is_binary_tree
from proof_machine.others.util import subset_list


def get_tree_signature(tree, leaves_indicator=None):
    """gets the parents and children signatures of a tree"""
    # signature is a pair of flatten list: parents, children
    if leaves_indicator is None or len(leaves_indicator) == 0:
        leaves_indicator = tree_to_leaves_indicator(tree)
        nodes_list = tree.flatten()
    else:
        nodes_list = tree.flatten(leaves_indicator)
    parents_indicator = [x == '0' for x in leaves_indicator]
    children_indicator = [x == '1' for x in leaves_indicator]
    return {'parentsSignature': subset_list(nodes_list, parents_indicator),
            'childrenSignature': subset_list(nodes_list, children_indicator)}


def view_signature(sign1):
    """views the parents and children signature"""
    print("Parents signature:")
    _ = [x.view() for x in sign1['parentsSignature']]
    print("Children signature:")
    for item in sign1['childrenSignature']:
        if is_binary_tree(item):
            item.key.view()
        else:
            item.view()


def tree_signature_test(sign1, sign2, quiet=True):
    """tests signature 1 against the benchmark / source signature (signature 2)"""
    if not quiet:
        print("============== Signature of input ==============")
        view_signature(sign1)
        print("===== Function internal signature register =====")
        view_signature(sign2)
        print("================================================")
        pps = compare_signature(sign1['parentsSignature'], sign2['parentsSignature'], "Parents")
        pcs = compare_signature(sign1['childrenSignature'], sign2['childrenSignature'], "Children")
        print("Pass parent signature? " + str(pps))
        print("Pass children signature? " + str(pcs))
        print("Pass both signature? " + str(pps and pcs))
        print("================================================")
    # signature is a pair of flatten list: parents, children
    return compare_signature(sign1['parentsSignature'], sign2['parentsSignature'], "Parents") and compare_signature(
        sign1['childrenSignature'], sign2['childrenSignature'], "Children")


def compare_signature(sign1, benchmark_sign, signature_type):
    """compares the signature 1 with signature 2"""
    compare_fun = compare_parents_nodes if signature_type == 'Parents' else compare_children_nodes
    for ind, item2 in enumerate(benchmark_sign):
        item1 = sign1[ind]
        item1 = item1.key if is_binary_tree(item1) else item1
        item2 = item2.key if is_binary_tree(item2) else item2
        if not compare_fun(item1, item2):
            return False
    return True


def compare_parents_nodes(node1, benchmark_node):
    """checks parents signature; returns True if symbol, ptype and state of the nodes are all equal"""
    return node1.value == benchmark_node.value and node1.ptype == benchmark_node.ptype and all(
        [x in node1.state for x in benchmark_node.state])


def compare_children_nodes(node1, benchmark_node):
    """checks children signature; returns True if the states of node 1 contains all the states of benchmark_node"""
    return all([x in node1.state for x in benchmark_node.state])
