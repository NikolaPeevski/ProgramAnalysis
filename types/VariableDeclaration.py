from types.Declaration import Declaration


class VariableDeclaration(Declaration):

    def __init__(self, name: str):
        super().__init__(name)
