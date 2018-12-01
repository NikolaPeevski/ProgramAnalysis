from microCTypes.Expression import Expression


class ArithmeticExpression(Expression):

    def __init__(self, entries: list):
        """
        :param entries: An array/list of ExpressionEntry
        """
        super().__init__('ArithmeticExpression')

        self.formattedExpression = entries

    def evaluateExpression(self):
        """
        If we need to compute functions this will be implemented,
        for the time being we don't care about it
        :return: Just a 0
        """
        return 0
