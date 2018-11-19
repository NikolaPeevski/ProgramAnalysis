from abc import ABC


class Statement(ABC):
    # TODO Implement this
    def __init__(self, name: str, _type: str):
        self.name = name
        self.type = _type

    def getName(self):
        return self.name

    def getType(self):
        return self.type