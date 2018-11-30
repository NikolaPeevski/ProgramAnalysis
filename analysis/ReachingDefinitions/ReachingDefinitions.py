import microCTypes as mt
from analysis.Analysis import Analysis
from analysis.Constraint import Constraint
from algorithms.Worklist import Worklist
from microCTypes import BaseNode
from microCTypes.Program import Program
from microCTypes import Statement
from microCTypes.VariableAssignmentStatement import VariableAssignmentStatement
from microCTypes.VariableDeclaration import VariableDeclaration

class ReachingDefinitions(Analysis):
    killSet = []
    genSet = []

    def __init__(self, program):
        """
        Base class for all program analysis
        Contains the abstract analyse method that performs
        the actual analysis step for the program
        :param program: The program to analyse
        """
        self.program = program

        self.contraints = []

        self.edges = []

        self.initialConstraints = []

        for programPoint in program: #      Create initial constrants based on variables across the program
            if type(programPoint) == VariableAssignmentStatement or type(programPoint) == VariableDeclaration: #        if it's a variable declaration or variable assignment
                new = (programPoint.getName(), "?") #       create new constraint
                if not self.initialConstraints.__contains__(new):  #        if the constraint is not already in the initial constraints - this would be the case with multiple assigments of variable X
                    self.initialConstraints.append(new) #       add the constraint



    def analyse(self, analyseObject):
        output = analyseObject[0].constraint.copy() #   Copy the constraints so we can work with them safely

        if type(analyseObject[1]) == VariableAssignmentStatement or type(analyseObject[1]) == VariableDeclaration: # If type variable assignment
            initialConstraints = analyseObject[0].constraint #    get the constraints we know from the node we're going from
            for constraint in initialConstraints: #     For all these constraints
                if constraint[0] == analyseObject[1].getName(): #       If the assignments variable is represented in a known constraint
                    output.remove(constraint) #     Remove that constraints - kill it
            genSet = (analyseObject[1].getName(), str(analyseObject[1].label)) #     create a genSet based on the name of variable and the label of the node we're going to
            output.append(genSet) #     Put the new constraint into the known constraints



        return output




