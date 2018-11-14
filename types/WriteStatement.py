from types.Statement import Statement


class WriteStatement(Statement):

    def __init__(self, statement: Statement):
        self.statement = statement