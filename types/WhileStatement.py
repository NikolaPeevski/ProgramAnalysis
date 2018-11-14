from types.BooleanExpression import BooleanExpression
from types.Statement import Statement


class WhileStatement(Statement):

    def __init__(self, boolean_expression: BooleanExpression, statement: Statement):
        self.boolean_expression = boolean_expression
        self.statement = statement
