from abc import ABC, abstractmethod

from analysis import Analysis, Constraint
from microCTypes.BaseNode import BaseNode
from microCTypes.Program import Program


class WorkList(ABC):

    def __init__(self, program: Program, analysis: Analysis):
        self.__program = program
        self.__analysis = analysis
        self.__worklist = []
        self.__constraints = []
        self.__influenced = []

    @abstractmethod
    def extract(self) -> BaseNode:
        pass

    @abstractmethod
    def insert(self, constraint) -> None:
        pass

    @abstractmethod
    def empty(self) -> bool:
        return len(self.__worklist) == 0

    def __analyse(self, step: BaseNode) -> Constraint:
        """
        Call the analysis object analysis method to analyse the current label
        :param step: The step to analyse
        :return: The constraints produced by the analysis object
        """
        return self.__analysis.__analyse(step)

    def iterate(self):

        for constraint, counter in self.__program.getNodes():
            self.insert(constraint)  # all constraints in the worklist
            # Empty set as the least value in the lattice. Don't know if this is correct?
            self.__constraints.append({})  # The least element of L
            self.__influenced.append({})

        # TODO: Implement the influence loop from Lecture 8 slide 15

        while not self.empty():

            next = self.extract()  # Consider the next constraint

            new = self.__analysis.__analyse(next)

            # TODO: Make the comparison is correct
            if self.__constraints[next.getLabel()] != new:  # Any work to do?

                # The slide depicts an union with the old constraints,
                # so this will have to be looked at if assignment is correct
                self.__constraints[next.getLabel()] = new  # Update the analysis info

                for next_infl in self.__influenced[next.getLabel()]:
                    self.insert(next_infl)  # Update the worklist
