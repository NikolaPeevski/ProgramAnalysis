from types.ComparativeOperator import ComparativeOperator
from types.Expression import Expression


class OperatorExpression(Expression):

    def __init__(self, left_hand_side: Expression, right_hand_side: Expression, operator: ComparativeOperator):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side
        self.operator = operator
