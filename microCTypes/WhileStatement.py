from microCTypes.BooleanExpression import BooleanExpression
from microCTypes.Statement import Statement


class WhileStatement(Statement):

    def __init__(self, boolean_expression: BooleanExpression, statement: Statement):
        super().__init__("While {}".format(boolean_expression.getExpression()), "WhileStatement")
        self.boolean_expression = boolean_expression
        self.statement = statement

    def getExpression(self):
        return self.boolean_expression

    def getSubStatement(self):
        return self.statement

    def expand(self):
        statements = []
        st = self.getSubStatement()

        if st is not None:
            statements = st.expand()
            statements.insert(0, st)

        return statements



