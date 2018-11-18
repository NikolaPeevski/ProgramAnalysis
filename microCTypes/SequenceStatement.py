from microCTypes.Statement import Statement


class SequenceStatement(Statement):

    def __init__(self, first_statement: Statement, second_statement: Statement):
        self.first_statement = first_statement
        self.second_statement = second_statement
