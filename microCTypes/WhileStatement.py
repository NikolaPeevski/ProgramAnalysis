from microCTypes.BooleanExpression import BooleanExpression
from microCTypes.Statement import Statement


class WhileStatement(Statement):

    def __init__(self, boolean_expression: BooleanExpression, statement: Statement):
        self.boolean_expression = boolean_expression
        self.statement = statement

    def getExpression(self):
        return self.boolean_expression

    def getStatement(self):
        return self.statement

