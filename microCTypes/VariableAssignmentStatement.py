from microCTypes.Statement import Statement
from microCTypes.ArithmeticExpression import ArithmeticExpression


class VariableAssignmentStatement(Statement):

    variable_name: str

    def __init__(self, variable_name: str, value: int):
        """

        :param variable_name:
        :param value: Integer
        """
        super().__init__(variable_name, "Variable")
        self.value = value

    def __init__(self, variable_name: str, value: ArithmeticExpression):
        """

        :param variable_name:
        :param value: ArithmeticExpression
        """
        super().__init__(variable_name, "Variable")
        self.value = value
