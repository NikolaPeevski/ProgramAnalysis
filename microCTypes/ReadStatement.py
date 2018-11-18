from microCTypes.Expression import Expression
from microCTypes.Statement import Statement


class ReadStatement(Statement):

    def __init__(self, expression: Expression):
        self.expression = expression
