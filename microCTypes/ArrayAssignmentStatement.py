from microCTypes.Statement import Statement
from microCTypes.ArithmeticExpression import ArithmeticExpression


class VariableAssignmentStatement(Statement):

    def __init__(self, array_name: str, index: int, value: ArithmeticExpression):
        """

        :param array_name:
        :param index:
        :param value:
        """
        super().__init__(array_name, "Array")
        self.index = index
        self.value = value

    def __init__(self, array_name: str, index: int, value: int):
        """

        :param array_name:
        :param index:
        :param value:
        """
        super().__init__(array_name, "Array")
        self.index = index
        self.value = value

    def getIndex(self):
        return self.index

    def getArrayName(self):
        return super().getName()

    def getValue(self):
        return self.value.getExpression() if type(self.value) == ArithmeticExpression else self.value
