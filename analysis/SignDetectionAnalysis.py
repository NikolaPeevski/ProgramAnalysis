from analysis.Analysis import Analysis
from microCTypes.BaseNode import BaseNode
from microCTypes.VariableDeclaration import VariableDeclaration
from microCTypes.WhileStatement import WhileStatement


class SignDetectionAnalysis(Analysis):

    def analyse(self, step: BaseNode):
        if isinstance(step, VariableDeclaration):
            print(f'Declaration at {step.getLabel()}')
        if isinstance(step, WhileStatement):
            print(f'While statement at {step.getLabel()}')
        else:
            try:
                print(f'Label {step.getLabel()}')
            except AttributeError:
                print('error')
