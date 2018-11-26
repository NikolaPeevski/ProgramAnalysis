from abc import ABC


class Constraint(ABC):

    def __init__(self, _name: object, _values: object) -> object:
        self.name = _name
        self.values = _values

    #def __init__(self, _name: object, ) -> object:
     #   self.name = _name
      #  self.value = 0

    def getName(self):
        return self.name

    def getValue(self):
        return self.values
