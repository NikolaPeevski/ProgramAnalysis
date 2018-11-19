from abc import ABC


class ExpressionEntry(ABC):

    def __init__(self, _type, symbol):
        self.type = _type
        self.symbol = symbol

    def getType(self):
        return self.type

    def getChar(self):
        return self.symbol
