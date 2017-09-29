"""This file contains the Session class"""

from .namespace import Namespace
from .functionspace import FunctionSpace

class Session:
    """This class is the environment that binds everything together."""
    def __init__(self):
        self.namespace = Namespace()
        self.functionspace = FunctionSpace(namespace=self.namespace)
