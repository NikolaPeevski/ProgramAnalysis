from microCTypes.BooleanExpression import BooleanExpression
from microCTypes.IfStatement import IfStatement
from microCTypes.Statement import Statement


class IfElseStatement(IfStatement):

    def __init__(self, boolean_expression: BooleanExpression, if_statement: Statement, else_statement: Statement):
        super().__init__(boolean_expression, if_statement)
        self.else_statement = else_statement

    def getIfStatement(self):
        return super().getStatement()

    def getElseStatement(self):
        return self.else_statement
