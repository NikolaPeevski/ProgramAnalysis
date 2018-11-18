from microCTypes.BooleanExpression import BooleanExpression
from microCTypes.Statement import Statement


class IfStatement(Statement):

    def __init__(self, boolean_expression: BooleanExpression, statement: Statement):
        self.statement = statement
        self.boolean_expression = boolean_expression
