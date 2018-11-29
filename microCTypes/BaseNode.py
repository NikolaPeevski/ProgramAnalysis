from abc import ABC


class BaseNode(ABC):

    def __init__(self, name: str, _type: str, parentNode, *node):
        self.name = name
        self.type = _type
        self.label = 0
        self.constraint = []
        # print(name)

        if parentNode is not None:
            self.parentNode = parentNode
        else:
            self.parentNode = None

        if node is not None and not isinstance(node, tuple):
            self.appendNode(node)
        else:
            self.nodes = []



    def getConstraint(self):
        return self.constraint

    def setConstraint(self, constraint):
        self.constraint = constraint

    def appendNode(self, node):

       # node.setParent(self)

        self.nodes.append(node)

        # print("Nodes are")
        # for i in self.nodes:
        #     print(i.getName())

    def setParent(self, parent):
        self.parentNode = parent

    def getParentNode(self):
        return self.parentNode

    def getNodes(self, counter: int = None):
        """
        Retrieves and labels all nodes
        :param counter: To keep count
        :return: Nodes array and counter
        """
        #  print(self.getName(), self.label)
        if counter is None:
            counter = 1

        if len(self.nodes) == 0:
            return None, counter

        res = []

        for i in self.nodes:
            i.label = counter
            counter += 1
            children, counter = i.getNodes(counter)

            if children is None:
                res.append(i)
            else:
                res.append([i, children])

            # print(i.getName(), i.getLabel(), res)

        return res, counter

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getNodesLen(self):
        return len(self.nodes)

    def getLabel(self):
        return self.label
