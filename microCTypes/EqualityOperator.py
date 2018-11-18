from microCTypes.Operator import Operator


class EqualityOperator(Operator):

    def __init__(self, operator: str):
        self.operator = operator
