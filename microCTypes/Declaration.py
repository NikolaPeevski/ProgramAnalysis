from microCTypes.baseNode import baseNode


class Declaration(baseNode):

    def __init__(self, name: str):
        super().__init__(name, "Declaration", None)
