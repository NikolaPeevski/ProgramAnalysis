from microCTypes.BaseNode import BaseNode


class Declaration(BaseNode):

    def __init__(self, name: str):
        super().__init__(name, "Declaration", None)
