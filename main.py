#!/usr/bin/env python3
"""
Module Docstring
"""
from algorithms.Worklist import Worklist
from algorithms.LIFO import LIFO
from algorithms.FIFO import FIFO
from analysis.SignDetection.SignDetection import SignDetection
from analysis.ReachingDefinitions.ReachingDefinitions import  ReachingDefinitions
from microCTypes.BooleanExpression import BooleanExpression
from microCTypes.EndNode import EndNode
from microCTypes.ExpressionEntry import ExpressionEntry
from microCTypes.Operator import Operator
from microCTypes.Program import Program
from microCTypes.Statement import Statement
from microCTypes.VariableAssignmentStatement import VariableAssignmentStatement
from microCTypes.VariableDeclaration import VariableDeclaration
from microCTypes.WhileStatement import WhileStatement
from microCTypes.ArithmeticExpression import ArithmeticExpression

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

    # lb1 = VariableAssignmentStatement("z", 5)
    #     #
    #     # lb2 = WhileStatement(BooleanExpression(
    #     #     [
    #     #         ExpressionEntry("Variable", "z"),
    #     #         ExpressionEntry(Operator("Relative", "=="), "=="),
    #     #         ExpressionEntry("Integer", "5")
    #     #     ])
    #     # )
    #     # lb3 = VariableAssignmentStatement("x", 5)
    #     # lb4 = WhileStatement(
    #     #     BooleanExpression([
    #     #         ExpressionEntry(Operator("Boolean", "true"), "true")
    #     #     ])
    #     # )
    #     # lb4_1 = WhileStatement(
    #     #     BooleanExpression([
    #     #         ExpressionEntry(Operator("Boolean", "true"), "true")
    #     #     ])
    #     # )
    #     # lb5 = Statement("Skip", "Skip")
    #     #
    #     # lb6 = VariableDeclaration("y")

    # graph = {program: [lb1],
    #          lb1: [lb2],
    #          lb2: [lb3, lb6],
    #          lb3: [lb2, lb4],
    #          lb4: [lb4_1, lb3],
    #          lb4_1: [lb5, lb4],
    #          lb5: [lb4_1],
    #          lb6: []
    #          }




    lb7 = EndNode("EndNode")
    lb7.constraint = []

    lb1 = VariableAssignmentStatement("y", 1)

    lb2 = WhileStatement(BooleanExpression(
        [
            ExpressionEntry("Variable", "y"),
            ExpressionEntry(Operator("Boolean", ">"), ">"),
            ExpressionEntry("Integer", "0")
        ]
    ))

    lb3 = VariableAssignmentStatement("y", ArithmeticExpression(
        [
            ExpressionEntry("Variable", "x"),
            ExpressionEntry(Operator("Arithmetic", "*"), "*"),
            ExpressionEntry("Variable", "y")
        ]
    ))

    lb4 = VariableAssignmentStatement("x", ArithmeticExpression(
        [
            ExpressionEntry("Variable", "x"),
            ExpressionEntry(Operator("Arithmetic", "-"), "-"),
            ExpressionEntry("Integer", "1")
        ]
    ))

    lb7 = EndNode("EndNode")
    lb7.constraint = []

    graph = {program: [lb1],
             lb1: [lb2],
             lb2: [lb3, lb7],
             lb3: [lb4],
             lb4: [lb7]
             }



    analysis = SignDetection(graph) #    Analysis is set to the analysis we want, ReachingDefinitions or SignDetection
    workList = FIFO(graph, analysis) #  Instantiate the work list as either FIFO (First in, First out) or LIFO (Last in, First out
    workList.worklist() #   Start the analysis

    print(" ")
    # representation parsing
    for i in graph:
        for x in i.constraint:
            for y in i.constraint:
                if x == y:
                    continue
                elif x[0] == y[0]:
                    badguy = list(x)
                    if not y[1].__contains__(x[1]):
                        badguy[1] = str(x[1]) + ", " +str(y[1])
                        i.constraint.append(tuple(badguy))
                        if i.constraint.__contains__(x):
                            i.constraint.remove(x)
                        if i.constraint.__contains__(y):
                            i.constraint.remove(y)


        print(i.constraint)

        # program.appendNode(lb1)

        # program.appendNode(lb2)

        # lb2.appendNode(lb4)
        # lb2.appendNode(lb6)
        # lb2.appendNode(lb3)
        # lb4.appendNode(lb5)
        # lb4_1.appendNode(lb5)
        # lb4.appendNode(lb4_1)

        # program.appendNode(lb1)

        # lb1.appendNode(lb2)

        # lb2.appendNode(lb3)

        # lb2.appendNode(lb6)

        # lb3.appendNode(lb4)

        # lb3.appendNode(lb2)

        # lb4.appendNode(lb4_1)

        # lb4.appendNode(lb3)

        # lb5.appendNode(lb4_1)

        # lb6.appendNode(lb7)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
