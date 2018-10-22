from types.Operator import Operator
from types.Statement import Statement
from types.StatementSequence import StatementSequence


class WhileStatement(Statement):

    def __init__(self, operator: Operator, body: StatementSequence):
        self.operator = operator
        self.body = body

    def draw(self):
        pass
