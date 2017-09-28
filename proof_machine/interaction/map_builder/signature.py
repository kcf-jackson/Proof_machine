""" This file contains the functions to handle the signature of a map / tree"""
from proof_machine.object.tree import is_binary_tree
from proof_machine.interaction.encode_tree import tree_to_base_three_code

def getTreeSignature(tree, leaves_code=None):
    # signature is a pair of nodes list: parents, children
    if leaves_code is None or len(leaves_code) == 0:
        base_three_codes = tree_to_base_three_code(tree)
        nodes_list = tree.get_nodes()
        parents_indicator = [x != '0' for x in base_three_codes]
        children_indicator = [x == '0' for x in base_three_codes]
    else:
        nodes_list = tree.get_nodes(leaves_code)
        parents_indicator = [x == '0' for x in leaves_code]
        children_indicator = [x == '1' for x in leaves_code]
    return {'parentsSignature': subset_list(nodes_list, parents_indicator), \
            'childrenSignature': subset_list(nodes_list, children_indicator)}


def view_signature(sign1):
    print("Parents signature:")
    [x.view() for x in sign1['parentsSignature']]
    print("Children signature:")
    for x in sign1['childrenSignature']:
        x.key.view() if isinstance(x, BinaryTree) else x.view()


def treeSignatureTest(sign1, sign2, quiet=True):
    # signature 2 is the benchmark / source signature
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
    # signature is a pair of get_nodes list: parents, children
    return compare_signature(sign1['parentsSignature'], sign2['parentsSignature'], "Parents") and \
           compare_signature(sign1['childrenSignature'], sign2['childrenSignature'], "Children")


def compare_signature(sign1, benchmarkSign, signatureType):
    compareFUN = compare_parents_nodes if signatureType == 'Parents' else compare_children_nodes
    for ind, n2 in enumerate(benchmarkSign):
        n1 = sign1[ind]
        n1 = n1.key if is_binary_tree(n1) else n1
        n2 = n2.key if is_binary_tree(n2) else n2
        if not compareFUN(n1, n2):
            return False
    return True


def compare_parents_nodes(node1, benchmark_node):
    # Parents signature checks equality in Symbol, Type and State of the Nodes.
    return node1.value == benchmark_node.value and node1.ptype == benchmark_node.ptype and \
           all([x in node1.state for x in benchmark_node.state])


def compare_children_nodes(node1, benchmark_node):
    # the states of node 1 must contain all the states of benchmark_node to pass the test
    return all([x in node1.state for x in benchmark_node.state])
