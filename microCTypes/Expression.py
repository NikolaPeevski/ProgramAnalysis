from abc import ABC


class Expression(ABC):
    type: str

    def __init__(self, _type: str):
        self.type = _type

    def getType(self):
        return self.type