from types.Statement import Statement


class ReadStatement(Statement):

    def __init__(self, name: str):
        self.name = name

    def draw(self):
        pass
