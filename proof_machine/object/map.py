"""This file contains the Map class"""
from proof_machine.interaction.map_builder.tree_map_builder import build_tree_mapping


class Map:
    """Represents relationship between mathematical expressions.
    Attributes:
        input (str), output (str), relation (str), name (str), description (str),
        namespace (Namespace), function (function)
    """

    def __init__(self, name, description=None):
        self.input = None
        self.output = None
        self.relation = None
        self.name = name
        self.description = description if description is not None else ''
        self.namespace = None
        self.function = None

    def view(self):
        """Prints out the attributes of the object."""
        print("Function  {:^26} \t maps {:^35} \t to {:^40}".format(self.name, self.input, self.output))
        print(self.description)

    def build(self, input_str, output_str, relation, namespace):
        """Builds a map between two expression"""
        self.input = input_str
        self.output = output_str
        self.relation = relation
        self.namespace = namespace
        self.function = build_tree_mapping(input_str, output_str, namespace)
