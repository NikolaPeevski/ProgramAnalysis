from abc import ABC, abstractmethod


class Analysis(ABC):

    def __init__(self, program):
        """
        Base class for all program analysis
        Contains the abstract analyse method that performs
        the actual analysis step for the program
        :param program: The program to analyse
        """
        self.program = program

        self.contraints = []

    @abstractmethod
    def analyse(self, step):
        """
        Perform the analysis and computes the constraints for the step at the current step
        :param step: The step to analyse
        """
        pass
