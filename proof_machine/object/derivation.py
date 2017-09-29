"""This file contains the Derivation class"""
from proof_machine.interaction.compare_tree import tree_diff, min_diff_tree
from proof_machine.interaction.parser import parse, tidy_view
from proof_machine.others import unique
from .tree import is_binary_tree


# TODO Refactor this class
class Derivation:
    """The Derivation class is a list of tree expression"""

    def __init__(self, tree, namespace):
        self.expr_list = [tree]
        self.namespace = namespace

    def view(self):
        """prints out the attributes of the object"""
        for ind, tree in enumerate(self.expr_list):
            if ind == 0:
                # tree.view()
                tidy_view(tree, self.namespace)
            else:
                # print('= ' + treeToString(tree))
                print('= ' + tidy_view(tree, self.namespace, False))

    # Basic operations
    def derive(self, fun):
        """applies a supplied function to the last tree on the list."""
        if len(self.expr_list) != 0:
            self.expr_list.append(fun(self.expr_list[-1]))

    def substitute(self, sub_tree, fun):
        """takes the last expression, replaces a specified substring / subtree by its transform"""
        if not is_binary_tree(sub_tree):
            sub_tree = parse(sub_tree, self.namespace)
        if len(self.expr_list) != 0:
            self.expr_list.append(substitute(self.expr_list[-1], sub_tree, fun(sub_tree), self.namespace))

    def replace(self, sub_tree, new_tree):
        """takes the last expression, replaces a specified substring / subtree by a substring / subtree"""
        if not is_binary_tree(sub_tree):
            sub_tree = parse(sub_tree, self.namespace)
        if not is_binary_tree(new_tree):
            new_tree = parse(new_tree, self.namespace)
        if len(self.expr_list) != 0:
            self.expr_list.append(substitute(self.expr_list[-1], sub_tree, new_tree, self.namespace))

    def remove_duplication(self):
        """removes duplicated expression (tree)"""
        self.expr_list = remove_duplication(self.expr_list, self.namespace)

    # Automatic derivation
    def blind_derive(self, fun_list, steps=5, quiet=True, randomized=True):
        """does derivation by randomly applying the supplied functions on the tree."""
        import random
        for _ in range(steps):
            tree_list = self.expr_list[-1].get_subtrees()
            for sub_tree in tree_list:
                list_len = len(fun_list)
                rind = random.sample(list(range(list_len)), list_len) if randomized else list(range(list_len))
                for ind in rind:
                    fun = fun_list[ind]
                    transformed_tree = fun(sub_tree)
                    if transformed_tree != sub_tree:
                        self.replace(sub_tree, transformed_tree)
                        if not quiet:
                            print(sub_tree.get_str() + ' -> ' + transformed_tree.get_str())
        self.remove_duplication()

    def semi_auto_derive(self, fun_list, quiet=True):
        """does derivation by applying all supplied functions on the tree then asking user to
        decide on one to proceed."""
        current = self.expr_list[-1]
        continue_flag = True
        while continue_flag:
            print("\n" + current.get_str() + " = ")
            new_list = remove_duplication(derive_new_expr(current, fun_list, self.namespace, quiet), self.namespace)
            for ind, new_expr in enumerate(new_list):
                print(str(ind + 1) + ": " + new_expr.get_str())
            choice = input("Which line do you want to continue with (Type 'q' to end)? ")
            if choice == 'q':
                continue_flag = False
                break
            elif 1 <= int(choice) <= len(new_list):
                current = new_list[int(choice) - 1]
                self.expr_list.append(current)
            else:
                continue

    def auto_derive(self, target_tree, fun_list, steps=5, quiet=True):
        """does automatic derivation based on minimisation the difference score between the
        source tree and the target tree."""
        for i in range(steps):
            current = self.expr_list[-1]
            print(("" if i == 0 else "= ") + current.get_str())
            new_list = remove_duplication(derive_new_expr(current, fun_list, self.namespace, quiet), self.namespace)
            self.expr_list.append(min_diff_tree(target_tree, new_list))
            if tree_diff(self.expr_list[-1], target_tree) == 0:
                break
        print("Difference score of the final expression and the target expression: " + str(
            tree_diff(self.expr_list[-1], target_tree)))


def auto_derive_breadth(derive_obj, fun_list, namespace, steps=5, quiet=True):
    """the underlying core code"""
    full_list = [[0, derive_obj.exprList[-1]]]
    for i in range(steps):
        sublist = subset_by_layer(full_list, i)
        for expr_with_meta in sublist:
            expr = expr_with_meta[1]
            new_list = remove_duplication(derive_new_expr(expr, fun_list, namespace, quiet), namespace)
            full_list += append_index_to_expr(new_list, i + 1)
    return full_list


def derive_new_expr(tree, fun_list, namespace, quiet=True):
    """given a tree and a list of functions, apply each function to all subtrees (when possible)
    then return the list of new expressions"""
    tree_list = tree.get_subtrees()
    res_list = []
    for sub_tree in tree_list:
        for _, fun in enumerate(fun_list):
            transformed_tree = fun(sub_tree)
            if transformed_tree != sub_tree:
                res_list.append(substitute(tree, sub_tree, transformed_tree, namespace))
                if not quiet:
                    print(sub_tree.get_str() + ' -> ' + transformed_tree.get_str())
    return res_list


# Helper functions
def subset_by_layer(full_list, i):
    """get all the tree at the same layer level."""
    return [item for item in full_list if item[0] == i]


def append_index_to_expr(expr_list, i):
    """adds a layer index to a tree showing the depth position."""
    return [[i, item] for item in expr_list]


def remove_duplication(tree_list, namespace):
    """turns trees into strings, removes duplicate str then converts the remaining back to trees."""
    str_list = [tree.get_str() for tree in tree_list]
    return [parse(x, namespace) for x in unique(str_list)]


def substitute(origin_tree, old_tree, new_tree, namespace):
    """replaces a part in the original tree by a new part."""
    # return parse(treeToString(origin_tree).replace(treeToString(old_tree), treeToString(new_tree)), namespace)
    new_expr = origin_tree.get_str().replace(old_tree.get_str(), new_tree.get_str())
    return parse(new_expr, namespace)
