from microCTypes.Operator import Operator


class EqualityOperator(Operator):
    # TODO Ask the group if we need this anymore
    
    def __init__(self, operator: str):
        self.operator = operator
