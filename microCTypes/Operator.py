from abc import ABC


class Operator(ABC):

    def __init__(self, operatortype: str, operator: str):
        self.operatorType = operatortype
        self.operator = operator

    def getOperator(self):
        return self.operator

    def getOperatorType(self):
        return self.operatorType

