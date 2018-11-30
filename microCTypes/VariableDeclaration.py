from microCTypes.Statement import Statement
from microCTypes.Variable import Variable


class VariableDeclaration(Statement):
    variable: Variable

    def __init__(self, name: str):
        super().__init__(name, '0')
        self.variable = Variable(name)


    def getVariable(self):
        return self.variable

