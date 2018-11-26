from analysis.Analysis import Analysis
from analysis.ReachingDefinitions.Constraint import Constraint
import microCTypes as mt


class ReachingDefinitions(Analysis):

    killSet = []
    genSet = []

    def analyse(self, step):


        if type(step) == mt.VariableAssignmentStatement.VariableAssignmentStatement:
            for constraint in self.contraints:
                if constraint.name == step.getName():
                      if not type(step.parentNode) == mt.WhileStatement.WhileStatement:
                        self.killSet = Constraint(constraint.name, [constraint.values])
            self.genSet = Constraint(step.getName(), [step.getLabel()])
            self.updateConstraints(self.killSet, self.genSet)
        print(self.contraints)

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




