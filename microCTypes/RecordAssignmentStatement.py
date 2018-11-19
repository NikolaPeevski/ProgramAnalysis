from microCTypes.Statement import Statement
from microCTypes.ArithmeticExpression import ArithmeticExpression


class VariableAssignmentStatement(Statement):

    def __init__(self, record_name: str, pointer: str, value: ArithmeticExpression):
        """

        :param record_name:
        :param pointer:
        :param value:
        """
        super().__init__(record_name, "Record")
        self.pointer = pointer
        self.value = value

    def __init__(self, record_name: str, pointer: str, value: int):
        """

        :param record_name:
        :param pointer:
        :param value:
        """
        super().__init__(record_name, "Record")
        self.pointer = pointer
        self.value = value

    def getPointer(self):
        return self.pointer

    def getValue(self):
        return self.value.getExpression() if type(self.value) == ArithmeticExpression else self.value
