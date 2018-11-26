from analysis.Analysis import Analysis
from analysis.ReachingDefinitions.Constraint import Constraint
import microCTypes as mt


class ReachingDefinitions(Analysis):

    killSet = {}
    genSet = {}

    def analyse(self, step):

        found = False
        if type(step) == mt.VariableAssignmentStatement.VariableAssignmentStatement:
            for constraint in self.contraints:
                if constraint.name == step.getName():
                      found == True
                      self.killSet = Constraint(constraint.name, constraint.values)
            self.genSet = Constraint(step.getName(), step.getLabel())
            self.updateConstraints(self.killSet, self.genSet)
        print(self.contraints)

    def updateConstraints(self, killSet, genSet):
        tempConstraints = self.contraints

        for constraint in self.contraints:
            for kill in killSet:
                if constraint.name == kill[0].name:
                    tempConstraints.remove(constraint)
        tempConstraints.append(genSet)
        self.contraints = tempConstraints




