from microCTypes.BooleanExpression import BooleanExpression
from microCTypes.Statement import Statement


class WhileStatement(Statement):

    def __init__(self, boolean_expression: BooleanExpression):
        super().__init__("While {}".format(boolean_expression.getExpression()), "WhileStatement")
        self.boolean_expression = boolean_expression

    def getExpression(self):
        return self.boolean_expression
