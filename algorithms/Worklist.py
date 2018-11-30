from abc import ABC

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

    # @abstractmethod
    def extract(self) -> BaseNode:
        """
        Extract the next constraint from the work list to be analysed
        """
        pass

    # @abstractmethod
    def insert(self, constraint) -> None:
        """
        Insert a constraint into the work item list
        :param constraint: The constraint to add
        """
        pass

    # @abstractmethod
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
        for x in self.__program:
            if type(x) == Program:  # If program, it's entry node
                x.setConstraint(
                    self.__analysis.initialConstraints)  # Gets the known constraints from the appropriate analysis
            else:
                x.constraint = []  # All other constraints are empty to start

        counter = 0
        for node in self.__program:
            node.label = counter  # Establishes labels for our nodes
            counter = counter + 1
            for neighbour in self.__program[node]:  # Worklist is supplemented with every edge from the collected nodes
                self.__worklist.append((node, neighbour))

        while not self.empty():

            next = self.__worklist[len(self.__worklist) - 1]  # LIFO worklist - Consider the next edge
            # next = self.__worklist[0]  # #FIFO worklist - Consider the next edge

            # for console printing only
            labeling = []
            RD0 = []
            for points in self.__worklist:
                labeling.append(str(points[0].getLabel()) + " to " + str(points[1].getLabel()))
            for point in self.__program:
                RD0.append(point.constraint)
            print(str(labeling) + " = " + str(RD0))
            ###

            self.__worklist.remove(next)  # Remove the edge from the worklist
            workedOn = False
            new = self.__analysis.analyse(next)  # Analyse step for the individual analysis

            # TODO: Make sure the comparison is correct
            if not next[1] is None:  # Null check
                for constraint in new:  # In case there is more than one new constraint
                    if not next[1].constraint.__contains__(constraint):  # Any work to do?
                        next[1].constraint.append(constraint)  # Put the analysed constraints into the following node
                        workedOn = True
                if workedOn == True:  # If we've had work
                    if not self.__program.get(next[1]) is None:  # Null check
                        for newEdge in self.__program.get(
                                next[1]):  # For the edges that go from the node we're going to
                            if not self.__worklist.__contains__(
                                    (next[1], newEdge)):  # If the edge is not already in the worklist
                                self.__worklist.append((next[1], newEdge))  # We add it
