from types.Expression import Expression
from types.Statement import Statement


class ReadStatement(Statement):

    def __init__(self, expression: Expression):
        self.expression = expression