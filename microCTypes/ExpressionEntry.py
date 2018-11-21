from abc import ABC


class ExpressionEntry(ABC):

    def __init__(self, _type, entry):
        self.type = _type
        self.entry = entry

    def getType(self):
        return self.type

    def getEntry(self):
        return self.entry
