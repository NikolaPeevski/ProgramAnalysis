from types.Expression import Expression
from types.IfStatement import IfStatement
from types.StatementSequence import StatementSequence


class IfElseStatement(IfStatement):

    def __init__(self, condition: Expression, body_if: StatementSequence, body_else: StatementSequence):
        super().__init__(condition, body_if)
        self.body_else = body_else
