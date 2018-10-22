from types.Expression import Expression
from types.Statement import Statement
from types.StatementSequence import StatementSequence


class IfStatement(Statement):

    def __init__(self, condition: Expression, body_if: StatementSequence):
        self.condition = condition
        self.body_if = body_if

    def draw(self):
        pass
