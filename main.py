#!/usr/bin/env python3
"""
Module Docstring
"""
from analysis.Analysis import Analysis
from microCTypes.VariableAssignmentStatement import VariableAssignmentStatement
from microCTypes.SequenceStatement import SequenceStatement
from microCTypes.Program import Program
from microCTypes.VariableDeclaration import VariableDeclaration

__author__ = "ProgramAnalysisGroup"
__version__ = "0.1."
__license__ = "MIT"


def main():

    program = Program("MyProgram1")
    program.makeDeclaration(VariableDeclaration('x'))
    program.makeStatement(VariableAssignmentStatement('x', 5))

    analysis = Analysis(program)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
