from microCTypes.Statement import Statement


class AssignmentStatement(Statement):

    def __init__(self, variable_name: str, value: int):
        self.variable_name = variable_name
        self.value = value
