from microCTypes.Expression import Expression


class ArithmeticExpression(Expression):
    formattedExpression: dict

    def __init__(self, _formattedExpression: dict):
        self.type = "ArithmeticExpression"
        self.formattedExpression = _formattedExpression
