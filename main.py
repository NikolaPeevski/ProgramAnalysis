#!/usr/bin/env python3
"""
Module Docstring
"""
from analysis.ReachingDefinitions.ReachingDefinitions import ReachingDefinitions
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
from microCTypes.Statement import Statement

__author__ = "ProgramAnalysisGroup"
__version__ = "0.1."
__license__ = "MIT"


def main():
    # TODO: Add variable declatation tracking, medium priority
    # TODO: Add expression usage tracking, medium priority
    # TODO: Add lattice generation, low priority unless demanded
    # TODO: Add lattice utils (parsing, node printing etc), low priority unless demanded
    # TODO: Add automated label assigning, low priority
    program = Program("MyProgram1")
    # xDeclaration = program.makeDeclaration(VariableDeclaration('z'))
    #
    # program.makeStatement(VariableAssignmentStatement(xDeclaration.getVariable(), ArithmeticExpression([ExpressionEntry("Variable", "x"), ExpressionEntry(Operator("Arithmetic", "+"), "+"), ExpressionEntry("Variable", "y")])))
    # program.makeStatement(WhileStatement(BooleanExpression([ExpressionEntry(Operator("Boolean", "true"), "true")]), Statement("skip", "skip")))
    # program.makeStatement(WhileStatement(BooleanExpression([ExpressionEntry(Operator("Boolean", "true"), "true")]), Statement("skip", "skip")))

    # print(program.toString())

    # For now I can't figure out how to label assign automated so we'll have to do it by hand
    label = 0;
    lb1 = VariableAssignmentStatement(Variable("z"), 5, 1)

    lb2 = WhileStatement(BooleanExpression(
        [ExpressionEntry("Variable", "Z"), ExpressionEntry(Operator("Relative", "="), "="),
         ExpressionEntry(Operator("Relative", "="), "="), ExpressionEntry("5", "5")]))
    lb3 = VariableAssignmentStatement(Variable("x"), 5, 3)
    lb4 = WhileStatement(BooleanExpression([ExpressionEntry(Operator("Boolean", "true"), "true")]))
    lb4_1 = WhileStatement(BooleanExpression([ExpressionEntry(Operator("Boolean", "true"), "true")]))
    lb5 = Statement("Skip", "Skip")
    lb4.appendNode(lb5)
    lb4_1.appendNode(lb5)
    lb4.appendNode(lb4_1)
    lb6 = VariableAssignmentStatement(Variable("z"), 6, 6)

    lb2.appendNode(lb3)

    program.appendNode(lb1)
    lb2.appendNode(lb4)
    lb2.appendNode(lb6)

    program.appendNode(lb2)

    program.getProgramBlocks()

    analysis = ReachingDefinitions(program)

    analysis.iterate(program.getNodes())
    for output in analysis.contraints:
        print(output.name + " = Label " + str(output.values))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
