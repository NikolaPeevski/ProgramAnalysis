class node():
    def __init__(self, label: int, action: object, nextNode: node):
        self.label = label
        self.action = action
        self.nextNode = nextNode

    def getLabel(self):
        return self.label

    def getAction(self):
        return self.action

    def getNextNode(self):
        return self.nextNode

