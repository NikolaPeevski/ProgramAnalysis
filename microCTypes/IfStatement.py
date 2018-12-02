from microCTypes.BooleanExpression import BooleanExpression
from microCTypes.Statement import Statement


class IfStatement(Statement):

    def __init__(self, boolean_expression: BooleanExpression):
        # self.statement = statement
        self.boolean_expression = boolean_expression

    def getExpression(self):
        return self.boolean_expression.getExpression()

    # def getStatement(self):
    #     return self.statement

    def evaluateExpression(self):
        return self.boolean_expression.evaluateExpression()
