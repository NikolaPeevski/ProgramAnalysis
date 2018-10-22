from types.Expression import Expression


class Variable(Expression):
    def __init__(self, name: str):
        self.name = name
