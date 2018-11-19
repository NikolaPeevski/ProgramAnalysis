from microCTypes.Declaration import Declaration


class RecordDeclaration(Declaration):
    # TODO Implement this

    def __init__(self, recordName: str, fst: int, snd: int):
        super().__init__(recordName)
        self.fst = fst
        self.snd = snd

    def getFst(self):
        return self.fst

    def getSnd(self):
        return self.snd
