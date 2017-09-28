class Session:
    def __init__(self):
        self.namespace = Namespace()
        self.functionSpace = FunctionSpace(namespace=self.namespace)
