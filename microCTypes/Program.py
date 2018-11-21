from microCTypes.Declaration import Declaration
from microCTypes.Statement import Statement
from microCTypes.WhileStatement import WhileStatement


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
        return dec

    def makeStatement(self, stat: Statement):
        self.programBlocks.append(stat)
        self.statements.append(stat.getName())
        return stat

    def toString(self):
        res = ""
        innerBlockCounter = 0

        for i in range(len(self.programBlocks)):
            block = self.programBlocks[i]

            # Could have special methods in the future
            if isinstance(block, Statement):
                res += '{} {}'.format(i + 1 + innerBlockCounter, self.programBlocks[i].getName())

                innerStatements = self.programBlocks[i].expand()

                for st_i in range(len(innerStatements)):
                    innerBlockCounter += 1
                    res += "\n"
                    res += '{} {}'.format(i + 1 + innerBlockCounter, innerStatements[st_i].getName())

            else:
                res += '{} {}'.format(i + 1 + innerBlockCounter, self.programBlocks[i].getName())

            res += "\n"

        return res

    def getProgramBlocks(self):
        return self.programBlocks
