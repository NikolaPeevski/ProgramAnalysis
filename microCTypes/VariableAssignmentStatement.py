from microCTypes.Statement import Statement
from microCTypes.Variable import Variable


class VariableAssignmentStatement(Statement):

    variable_name: str

    def __init__(self, variable, value):
        """
        :param variable_name:
        :param value: ArithmeticExpression
        """

        if type(variable) == Variable:
            if type(value) == int:
                super().__init__(variable, value)
            else:
                super().__init__(variable, value)
        else:
            if type(value) == int:
                super().__init__(variable, value)
            else:
                super().__init__(variable, value)


        # super().__init__(variable.getName() + value.getExpression(), "Variable")
        if not type(variable) == str:
            variable.value = value





