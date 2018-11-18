from microCTypes.Operator import Operator


class BooleanOperator(Operator):

    def __init__(self, operator: str):
        self.operator = operator
        self.operatorType = ""