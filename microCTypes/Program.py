from microCTypes.Declaration import Declaration
from microCTypes.Statement import Statement


class Program:
    programBlocks: [] = []
    declarations: [] = []
    statements: [] = []

    # TODO Implement this
    def __init__(self, declaration: Declaration = None, statement: Statement = None):
        self.statement = statement
        self.declaration = declaration

    def __init__(self, name: str):
        self.name = name

    def makeDeclaration(self, dec: Declaration):
        self.programBlocks.append(dec)
        self.declarations.append(dec.getName())
        pass

    def makeStatement(self, stat: Statement):
        self.programBlocks.append(stat)
        self.statements.append(stat.getName())
        pass

    def toString(self):
        res = ""

        for i in range(len(self.programBlocks)):
            res += '{} {}' % (i, self.programBlocks[i])
