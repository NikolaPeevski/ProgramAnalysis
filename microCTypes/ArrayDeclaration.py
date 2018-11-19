from microCTypes.Declaration import Declaration


class ArrayDeclaration(Declaration):

    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def getName(self):
        return super().getName()

    def getSize(self):
        return self.size
