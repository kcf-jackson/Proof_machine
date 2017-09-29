"""This file contains the FunctionSpace class"""
from proof_machine.interaction.map_builder import build_tree_mapping


# TODO Refactor this class
class FunctionSpace:
    """keeps track of the mappings between trees.

    Attributes:
        functionList, namespace
    """

    def __init__(self, namespace):
        self.functionList = {}
        self.namespace = namespace

    def add_function(self, example):
        """ adds function to the functionList

        The function takes a list of form [input, output, function name] or [input, output, [name_1, name2]].
        In the former case, it adds a tree mapping (from input to output) with the name 'function name';
        in the latter case, it add two mappings, one with the usual direction and one with the reverse direction (of input, output).
        """
        input_str = example[0]
        output_str = example[1]
        name_str = example[2]
        if len(name_str) == 2:
            self.functionList[name_str[0]] = build_tree_mapping(input_str, output_str, self.namespace)
            self.functionList[name_str[1]] = build_tree_mapping(output_str, input_str, self.namespace)
            print("Added function:  {:^26} \t that maps {:^35} \t to {:^40}".format(name_str[0], input_str, output_str))
            print("Added function:  {:^26} \t that maps {:^35} \t to {:^40}".format(name_str[1], output_str, input_str))
        else:
            self.functionList[name_str] = build_tree_mapping(input_str, output_str, self.namespace)
            print("Added function:  {:^26} \t that maps {:^35} \t to {:^40}".format(name_str, input_str, output_str))

    def add_list_of_functions(self, example_list):
        """ add a list of functinos to the functionList. """
        [self.add_function(x) for x in example_list]
