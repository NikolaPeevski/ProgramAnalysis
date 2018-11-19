from microCTypes.Operator import Operator


class BooleanOperator(Operator):

    def __init__(self, operator: str):
        super().__init__("Boolean", operator)

    def getOperator(self):
        return super().operator

    def getOperatorType(self):
        return super().operatorType
