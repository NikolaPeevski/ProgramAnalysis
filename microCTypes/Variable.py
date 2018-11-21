from abc import ABC


class Variable(ABC):
    name: str

    def __init__(self, _name: str, _value):
        self.name = _name
        self.value = _value

    def __init__(self, _name: str,):
        self.name = _name
        self.value = 0

    def getName(self):
        return self.name

    def getType(self):
        return self.value
