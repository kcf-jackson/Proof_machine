"""This file contains functions to create the mapping between two strings / trees."""
from proof_machine.interaction.encode_tree import base_three_code_to_tree
from proof_machine.interaction.encode_tree import tree_to_base_three_code, tree_to_leaves_indicator
from proof_machine.interaction.infer_state import infer_state
from proof_machine.interaction.map_builder.signature import getTreeSignature, treeSignatureTest
from proof_machine.interaction.parser.tree_parser import parse
from proof_machine.object.namespace import lookup_ptype
from proof_machine.object.node import Node
from proof_machine.others import which


def build_tree_mapping(expr1, expr2, namespace):
    """
    takes 2 input strings, parses them into trees and
    returns a function mapping the 1st tree to the 2nd tree
    """
    tree1 = parse(expr1, namespace)
    tree2 = parse(expr2, namespace)
    map_spec = get_nodes_mapping(tree1, tree2)
    extra_nodes = convert_symbol_to_nodes(map_spec['extraSym'], namespace)
    source_signature = getTreeSignature(tree1)
    source_tree_code = tree_to_leaves_indicator(tree1)
    target_map_code = tree_to_base_three_code(tree2)

    def tree_function(tree, quiet=True):
        """checks the signature and applies the tree mapping if the check passes."""
        tree = infer_state(tree)
        tree_signature = getTreeSignature(tree, source_tree_code)
        signature_pass = treeSignatureTest(tree_signature, source_signature, quiet)
        if signature_pass:
            nodes_list = tree.get_nodes(source_tree_code) + extra_nodes
            res = generic_tree_mapping(nodes_list, target_map_code, map_spec['map_dict'])
            return res
        else:
            return tree

    return tree_function


# Layer 1
def convert_symbol_to_nodes(symbol_list, namespace):
    """Converts list of symbols to list of get_nodes"""
    return [Node(symbol, lookup_ptype(symbol, namespace)) for symbol in symbol_list]


def get_nodes_mapping(tree1, tree2):
    """Find the extra symbols in the 2nd tree and the mapping from the 1st tree to the 2nd tree"""
    a1_sym = get_symbol_list(tree1)
    a2_sym = get_symbol_list(tree2)
    extra_sym = sym_diff(a1_sym, a2_sym)
    map_dict = find_mapping(a1_sym + extra_sym, a2_sym)
    return {'extra_sym': extra_sym, 'map_dict': map_dict}


def generic_tree_mapping(nodes_list, tree_map_code, nodes_dict):
    # creates a tree based on tree_map_code and put the nodes_list into it according to nodes_dict
    res_tree = base_three_code_to_tree(tree_map_code)
    target_nodes_list = map_nodes(nodes_list, nodes_dict)
    return res_tree.relabel_nodes(target_nodes_list)


# Layer 2
def get_symbol_list(tree):
    """Converts a tree into list of symbols"""
    nodes_list = treeToNodes(tree)
    sym_list = [x.value for x in nodes_list]
    return sym_list


def sym_diff(sym_list_1, sym_list_2):
    """Finds the extra symbols in symbol list 2"""
    return sorted(list(set(sym_list_2) - set(sym_list_1)))


def find_mapping(sym_list_1, sym_list_2):
    """finds the possible mapping from symbol list 1 to symbol list 2"""
    map_dict = {}
    for ind, sym in enumerate(sym_list_2):
        matched_pos = [k + 1 for k in which(sym_list_1, sym)]
        map_dict[ind + 1] = matched_pos[0]  # pick the first element if there is multiple match
    return map_dict


def map_nodes(nodes_list, nodes_dict):
    """permutes the nodes_list according to the supplied dictionary"""
    res_list = []
    for _, key in enumerate(nodes_dict):
        res_list.append(nodes_list[nodes_dict[key] - 1])  # must be in order
    return res_list
