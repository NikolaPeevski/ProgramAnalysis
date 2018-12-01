from analysis.Analysis import Analysis
from microCTypes.ArithmeticExpression import ArithmeticExpression
from microCTypes.BooleanExpression import BooleanExpression
from microCTypes.IfElseStatement import IfElseStatement
from microCTypes.IfStatement import IfStatement
from microCTypes.Statement import Statement
from microCTypes.VariableAssignmentStatement import VariableAssignmentStatement
from microCTypes.VariableDeclaration import VariableDeclaration
from microCTypes.WhileStatement import WhileStatement


class SignDetection(Analysis):

    def __init__(self, program):

        self.contraints = []

        self.edges = []

        self.initialConstraints = []

        for programPoint in program:  # Create initial constrants based on variables across the program
            if isinstance(programPoint, (
            VariableAssignmentStatement, VariableDeclaration)):  # if it's a variable declaration or variable assignment
                new = (programPoint.getName(), {'-', '0', '+'})  # create new constraint
                self.initialConstraints.append(new)  # add the constraint

    def isType(self, variable, t) -> bool:
        return type(variable) == t

    def lookUpConstraint(self, needle: str, constraints) -> tuple:
        for constraint in constraints:
            if needle == constraint[0]:
                return constraint
        return None

    def handleArithmeticExpression(self, expression: ArithmeticExpression, name: str, constraint: tuple, constrains):

        expressions = expression.formattedExpression

        for e in expressions:
            if e.getType().lower() == 'variable':
                constraint = constraint + self.lookUpConstraint(e.getEntry(), constrains)

    def handleBooleanExpression(self, step: list, output, booleanExpression: BooleanExpression):

        expressions = booleanExpression.formattedExpression

        length = len(expressions)

        result = {}

        for constraint in output:
            step_name = step[1].getName()
            new_value = constraint

            if constraint[0] == step_name:
                if length == 3:
                    new_value = (
                        expressions[0].getEntry(),
                        self.handleVariableComparison(
                            expressions[0].getEntry(),
                            expressions[1].getEntry(),
                            expressions[2].getEntry()
                        )
                    )
            output.remove(constraint)
            output.append(new_value)

        return output

    def handleVariableComparison(self, value, operator, comparison):

        comparison = int(comparison) if type(comparison) == str else comparison

        result = None

        if operator == '==':
            result = self.handleInteger(comparison)
        elif operator == '>=':
            if comparison > 0:
                result = {'+'}
            elif comparison < 0:
                result = {'-', '0', '+'}
            else:
                result = {'0', '+'}
        elif operator == '<=':
            if comparison > 0:
                result = {'+', '0', '-'}
            elif comparison < 0:
                result = {'-'}
            else:
                result = {'0', '+'}
        elif operator == '>':
            if comparison > 0:
                result = {'+'}
            if comparison < 0:
                result = {'-', '0', '+'}
            else:
                result = {'+'}
        elif operator == '<':
            if comparison > 0:
                result = {'-', '0', '+'}
            if comparison < 0:
                result = {'-'}
            else:
                result = {'0', '+'}

        return result

    def handleInteger(self, value):
        value = int(value)
        if value > 0:
            return {'+'}
        elif value < 0:
            return {'-'}
        else:
            return {'0'}

    def handleAssignment(self, step, output: list, next):

        for constraint in output:
            step_name = step[1].getName()
            step_value = step[1].getType()
            new_value = constraint
            if constraint[0] == step_name:
                if isinstance(step_value, ArithmeticExpression):  # Some how won't check for type or instance
                    c = self.handleArithmeticExpression(step_value, step_name, new_value, output)
                    c = {'+', '-'}
                else:
                    c = self.handleInteger(step_value)
                new_value = (step_name, c)

            output.remove(constraint)
            output.append(new_value)

        return output

    def analyse(self, step):

        output = step[0].constraint.copy()  # Copy the constraints so we can work with them safely

        next = step[1]

        if isinstance(next, (VariableDeclaration, VariableAssignmentStatement)):
            output = self.handleAssignment(step, output, next)

        if isinstance(next, WhileStatement):
            output = self.handleBooleanExpression(step, output, next.getExpression())

        if isinstance(next, (IfElseStatement, IfStatement)):
            output = self.handleBooleanExpression(step, output, next.getExpression())

        if isinstance(next, Statement) and next.getType() == 'skip':
            return output

        return output
