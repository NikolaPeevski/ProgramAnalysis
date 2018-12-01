from algorithms.Worklist import Worklist
from analysis.Analysis import Analysis
from microCTypes.BaseNode import BaseNode


class LIFO(Worklist):

    def __init__(self, program, analysis: Analysis):
        """
        The Last-in Last-out worklist algorithm
        :param program: The program to analyse
        :param analysis: The analysis to apply to the program
        """
        super().__init__(program, analysis)

    def insert(self, constraint) -> None:
        self.worklist_items.append(constraint)

    def extract(self) -> BaseNode:
        return self.worklist_items[len(self.worklist_items) - 1]
