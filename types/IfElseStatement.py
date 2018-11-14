from types.BooleanExpression import BooleanExpression
from types.IfStatement import IfStatement
from types.Statement import Statement


class IfElseStatement(IfStatement):

    def __init__(self, boolean_expression: BooleanExpression, if_statement: Statement, else_statement: Statement):
        super().__init__(boolean_expression, if_statement)
        self.else_statement = else_statement
