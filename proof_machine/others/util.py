"""This file contains the utility functions used by all other modules"""


def get_class(obj):
    """ Returns the class name of an object """
    return obj.__class__.__name__


def is_float(value):
    """ Check if an input is a float """
    try:
        float(value)
        return True
    except ValueError:
        return False


def subset_list(list0, indicator):
    """Subsets a list based on list of True / False"""
    return [node for ind, node in enumerate(list0) if indicator[ind]]


# R functions
def unique(list0):
    """ Returns a list of unique elements """
    from orderedset import OrderedSet
    return list(OrderedSet(list0))


def map2(list1, list2, fun):
    """ Functional programming helper """
    res = [fun(list1[ind], list2[ind]) for ind, _ in enumerate(list1)]
    return sum(res, [])


def which(list0, element):
    """ Returns a list of matching indexes """
    return [ind for ind, i in enumerate(list0) if i == element]
