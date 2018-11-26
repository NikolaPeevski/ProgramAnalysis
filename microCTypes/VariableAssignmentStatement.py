from microCTypes.Statement import Statement
from microCTypes.Variable import Variable
from microCTypes.ArithmeticExpression import ArithmeticExpression


class VariableAssignmentStatement(Statement):


    variable_name: str

    def __init__(self, variable, value, label):
        """

        :param variable_name:
        :param value: ArithmeticExpression
        """
        self.label = label
        if type(variable) == Variable:
            if type(value) == int:
                super().__init__(variable.getName(), value)
            else:
                super().__init__(variable.getName(), value)
        else:
            if type(value) == int:
                super().__init__("{} = {}".format(variable, value), "Variable Assignment")
            else:
                super().__init__("{} = {}".format(variable, value.getExpression()), "Variable Assignment")


        # super().__init__(variable.getName() + value.getExpression(), "Variable")
        if not type(variable) == str:
            variable.value = value





