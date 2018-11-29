from abc import ABC, abstractmethod

from analysis.Constraint import Constraint
from microCTypes.Program import Program


class Analysis(ABC):

    def __init__(self, program: Program):
        """
        Base class for all program analysis
        Contains the abstract analyse method that performs
        the actual analysis step for the program
        :param program: The program to analyse
        """
        self.program = program

        self.contraints = []

        self.analyse(program.getNodes())

    def iterate(self, iteration):
        """
        Iterate through the program parts
        For each iteration the analyse method is called
        :param iteration: The iteration step
        """
        if type(iteration) == list:
            for i in iteration:
                self.iterate(i)
        else:
            self.analyse(iteration)

    @abstractmethod
    def analyse(self, step) -> Constraint:
        """
        Perform the analysis and computes the constraints for the step at the current step
        :param step: The step to analyse
        """
        pass
