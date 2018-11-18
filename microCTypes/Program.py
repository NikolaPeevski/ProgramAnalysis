from microCTypes.Declaration import Declaration
from microCTypes.Statement import Statement


class Program:

    def __init__(self, declaration: Declaration = None, statement: Statement = None):
        self.statement = statement
        self.declaration = declaration
