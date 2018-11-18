from microCTypes.Declaration import Declaration


class ArrayDeclaration(Declaration):

    def __init__(self, size: int):
        super().__init__('A')
        self.size = size
