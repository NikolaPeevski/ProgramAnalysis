from abc import ABC


class Worklist(ABC):

    worklist:[] = []

    # TODO Implement this
    def __init__(self):
        pass

    def isEmpty(self):
        return len(self.worklist) == 0

    def insert(self, constraint):
        self.worklist.append(constraint)

        return self.worklist

    def extractFIFO(self, constraint):
        # TODO Implement this
        pass

    def extractLIFO(self, constraint):
        # TODO Implement this
        pass

    def iterate(self, list, analysis, ):
        # TODO Implement this
        pass