from microCTypes.Declaration import Declaration


class RecordDeclaration(Declaration):

    def __init__(self, fst: int, snd: int):
        super().__init__('R')
        self.fst = fst
        self.snd = snd

