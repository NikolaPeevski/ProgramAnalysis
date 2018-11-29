from abc import ABC, abstractmethod

from analysis import Analysis, Constraint
from microCTypes.BaseNode import BaseNode
from microCTypes.Program import Program


class Worklist(ABC):

    def __init__(self, program: Program, analysis: Analysis):
        """
        Abstract base class for all Worklist algorithms
        :param program: The program to analyse
        :param analysis: The analysis to apply to the program
        """
        self.__program = program  # The actual program that needs to be analysed
        self.__analysis = analysis  # The analysis we want to apply to the program
        self.__worklist = []  # Array containing the work list items
        self.__constraints = []  # The updated constraints for each work list
        self.__influenced = []  # Influenced variables

    @abstractmethod
    def extract(self) -> BaseNode:
        """
        Extract the next constraint from the work list to be analysed
        """
        pass

    @abstractmethod
    def insert(self, constraint) -> None:
        """
        Insert a constraint into the work item list
        :param constraint: The constraint to add
        """
        pass

    @abstractmethod
    def empty(self) -> bool:
        """
        Check if the work list is empty
        :return: True if the work list is empty, false if it is not empty
        """
        return len(self.__worklist) == 0

    def __analyse(self, step: BaseNode) -> Constraint:
        """
        Call the analysis object analysis method to analyse the current label
        :param step: The step to analyse
        :return: The constraints produced by the analysis object
        """
        return self.__analysis.__analyse(step)

    def worklist(self):
        """
        The general work list algorithm implemented according to lecture 8 slide 15
        """
        for constraint, counter in self.__program.getNodes():
            self.insert(constraint)  # all constraints in the worklist
            # TODO: Empty set as the least possible value in the lattice. Don't know if this is correct?
            self.__constraints.append({})  # The least element of L
            self.__influenced.append({})

        # TODO: Implement the influence loop from Lecture 8 slide 15

        while not self.empty():

            next = self.extract()  # Consider the next constraint

            new = self.__analysis.__analyse(next)

            # TODO: Make sure the comparison is correct
            if self.__constraints[next.getLabel()] != new:  # Any work to do?

                # The slide depicts an union with the old constraints,
                # so this will have to be looked at if assignment is correct
                self.__constraints[next.getLabel()] = new  # Update the analysis info

                for next_infl in self.__influenced[next.getLabel()]:
                    self.insert(next_infl)  # Update the worklist
