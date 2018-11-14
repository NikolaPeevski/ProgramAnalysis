from types.Declaration import Declaration
from types.Statement import Statement


class Program:

    def __init__(self, declaration: Declaration = None, statement: Statement = None):
        self.statement = statement
        self.declaration = declaration
