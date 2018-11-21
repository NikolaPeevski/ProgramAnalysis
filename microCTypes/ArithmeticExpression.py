from microCTypes.Expression import Expression
from microCTypes.ExpressionEntry import ExpressionEntry


class ArithmeticExpression(Expression):
    formattedExpression: [] = []

    def __init__(self, entries: []):
        """
        :param entries: An array/list of ExpressionEntry
        """
        super().__init__("ArithmeticExpression")
        self.formattedExpression = entries

    def getExpression(self):
        """
        :return: Something like x+5
        """
        expression = ""

        for i in self.formattedExpression:
            expression += i.getEntry()

        return expression

    def getName(self):
        return self.getExpression()

    def evaluateExpression(self):
        """
        If we need to compute functions this will be implemented,
        for the time being we don't care about it
        :return: Just a 0
        """
        return 0
