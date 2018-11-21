from abc import ABC


class Worklist(ABC):

    worklist:[] = []

    # TODO Implement this
    def __init__(self):
        pass

    def __init__(self, _worklist):
        self.worklist = _worklist

    def isEmpty(self):
        """
        Slightly modififed from simply empty which returns an empty list
        :return:
        """
        return len(self.worklist) == 0

    def insertFIFO(self, constraint):
        self.worklist.append(constraint)

        return self.worklist

    def insertLIFO(self, constraint):
        self.worklist.insert(0, constraint)

        return self.worklist

    def extractFIFO(self):
        """
        Using First in first out principle
        :return:
        """
        if self.isEmpty():
            return []

        condition = self.worklist.pop(0)

        # Remove occurences
        for i in range(len(self.worklist)):
            if condition == self.worklist[i]:
                self.worklist.pop(i)

        return condition, self.worklist

    def extractLIFO(self, constraint):
        """
        Using Last in first out principle
        :param constraint:
        :return:
        """
        if self.isEmpty():
            return []

        condition = self.worklist.pop()

        # Remove occurences
        for i in range(len(self.worklist)):
            if condition == self.worklist[i]:
                self.worklist.pop(i)

        return condition, self.worklist

    def iterate(self, list, analysis, ):
        # TODO Implement this
        pass