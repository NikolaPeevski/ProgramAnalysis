from types.Expression import Expression
from types.Statement import Statement


class AssignmentStatement(Statement):

    def __init__(self, variable: Expression, value):
        self.variable = variable
        self.value = variable

    def draw(self):
        pass
