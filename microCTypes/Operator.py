from abc import ABC


class Operator(ABC):

    def __init__(self, operatortype: str, operator: str):
        """

        :param operatortype: Arithmetic, Relational or Boolean
        :param operator: type-wise operator, > < == for Relational etc
        """
        self.operatorType = operatortype
        self.operator = operator

    def getOperator(self):
        """

        :return: Operator
        """
        return self.operator

    def getOperatorType(self):
        """

        :return: Arithmetic, Relational or Boolean
        """
        return self.operatorType
