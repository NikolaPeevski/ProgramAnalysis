from microCTypes.Variable import Variable
from microCTypes.Statement import Statement


class VariableDeclaration(Statement):
    variable: Variable

    def __init__(self, name: str, value: str):
        super().__init__(name, value)
        self.variable = Variable(name)


    def getVariable(self):
        return self.variable

