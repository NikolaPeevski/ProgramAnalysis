from microCTypes.Variable import Variable
from microCTypes.Statement import Statement


class VariableDeclaration(Statement):
    variable: Variable

    def __init__(self, name: str):
        super().__init__(name, "Variable declaration")
        self.variable = Variable(name)

    def getVariable(self):
        return self.variable

    def getName(self):
        return self.variable.getName()

