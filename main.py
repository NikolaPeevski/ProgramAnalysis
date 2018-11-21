#!/usr/bin/env python3
"""
Module Docstring
"""
from analysis.Analysis import Analysis
from microCTypes.VariableAssignmentStatement import VariableAssignmentStatement
from microCTypes.ArithmeticExpression import ArithmeticExpression
from microCTypes.SequenceStatement import SequenceStatement
from microCTypes.Program import Program
from microCTypes.VariableDeclaration import VariableDeclaration
from microCTypes.ExpressionEntry import ExpressionEntry
from microCTypes.Operator import Operator
from microCTypes.Variable import Variable
from microCTypes.WhileStatement import WhileStatement
from microCTypes.BooleanExpression import BooleanExpression
from microCTypes.Statement import  Statement

__author__ = "ProgramAnalysisGroup"
__version__ = "0.1."
__license__ = "MIT"


def main():
    # TODO: Add variable declatation tracking
    # TODO: Add expression usage tracking
    # TODO: Add lattice generation
    # TODO: Add lattice utils (parsing, node printing etc)
    program = Program("MyProgram1")
    xDeclaration = program.makeDeclaration(VariableDeclaration('z'))

    program.makeStatement(VariableAssignmentStatement(xDeclaration.getVariable(), ArithmeticExpression([ExpressionEntry("Variable", "x"), ExpressionEntry(Operator("Arithmetic", "+"), "+"), ExpressionEntry("Variable", "y")])))
    program.makeStatement(WhileStatement(BooleanExpression([ExpressionEntry(Operator("Boolean", "true"), "true")]), Statement("skip", "skip")))
    program.makeStatement(WhileStatement(BooleanExpression([ExpressionEntry(Operator("Boolean", "true"), "true")]), Statement("skip", "skip")))

    print(program.toString())

    analysis = Analysis(program)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
