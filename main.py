#!/usr/bin/env python3
"""
Module Docstring
"""
from analysis.Analysis import Analysis
from types.AssignmentStatement import AssignmentStatement
from types.SequenceStatement import SequenceStatement
from types.Program import Program
from types.VariableDeclaration import VariableDeclaration

__author__ = "ProgramAnalysisGroup"
__version__ = "0.1."
__license__ = "MIT"


def main():

    program = Program(
        VariableDeclaration('x'),
        AssignmentStatement('x', 5)
    )

    analysis = Analysis(program)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
