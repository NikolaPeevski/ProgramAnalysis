import microCTypes as mt
from analysis.Analysis import Analysis
from analysis.Constraint import Constraint
from algorithms.Worklist import Worklist
from microCTypes import BaseNode
from microCTypes.Program import Program
from microCTypes import Statement

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
        counter = 0
        for node in program:
            node.label = counter
            counter = counter+1
            for neighbour in program[node]:
                self.edges.append((node, neighbour))

        # self.analyse(program.getNodes())

    def startAnalysis(self):
#        initialConstraints = [0, Constraint("x", "?"), Constraint["y", "?"].Constraint["z", "?"]]
 ##          initialConstraints.append(x.getLabel(), [])
        for x in self.program:
            if type(x) == Program:
                x.setConstraint([("x", "?"), ("y", "?"), ("z", "?")])
            else:
                x.constraint = []
        workList = Worklist(self.program, self, self.edges)
        workList.worklist()

    def analysenew(self, analyseObject):
        output = analyseObject[0].constraint.copy()
        if type(analyseObject[1]) == mt.Statement.Statement:
            hej = 0
        if type(analyseObject[1]) == mt.VariableAssignmentStatement.VariableAssignmentStatement:
            initialConstraints = analyseObject[0].constraint
            for constraint in initialConstraints:
                if constraint[0] == analyseObject[1].getName():
                    output.remove(constraint)
            genSet = (analyseObject[1].getName(), analyseObject[1].label)
            output.append(genSet)
        return output

#isn't used atm, but still using as reference.
    def analyse(self, step, constraints):
        genSet = []
        output = constraints.copy()
        if type(step) == mt.VariableAssignmentStatement.VariableAssignmentStatement:
            for constraint in self.contraints:
                if constraint.name == step.getName() and constraint.getValue() == step.getValue():
                    output.remove(constraint)
            self.genSet = {step.getName(), [step.getLabel()]}
            output.append(genSet)
        return output

    def updateConstraints(self, killSet, genSet):
        tempConstraints = self.contraints
        found = False
        if not killSet == []:
            for constraint in self.contraints:
                if constraint.name == killSet.name:
                    tempConstraints.remove(constraint)
        if not genSet == []:
            for constraint in tempConstraints:
                if constraint.name == genSet.name:
                    constraint.values.append(genSet.values[0])
                    found = True
            if not found:
                tempConstraints.append(genSet)
        self.contraints = tempConstraints
