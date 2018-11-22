from abc import ABC

class baseNode(ABC):

    def __init__(self, name: str, _type: str, parentNode, *node):
        self.name = name
        self.type = _type
        # print(name)

        if parentNode is not None:
            self.parentNode = parentNode
        else:
            self.parentNode = None

        if node is not None and not isinstance(node, tuple):
            self.appendNode(node)
        else:
            self.nodes = []

    def appendNode(self, node):
        # print("{} node appended to parent {}. Nodes before appends are {}".format(node.getName(), self.getName(), self.getNodesLen()))
        node.setParent(self)
        self.nodes.append(node)

        # print("Nodes are")
        # for i in self.nodes:
        #     print(i.getName())

    def setParent(self, parent):
        self.parentNode = parent

    def getParentNode(self):
        return self.parentNode

    def getNodes(self):
        if len(self.nodes) == 0:
            return None

        res = []

        for i in self.nodes:
            print(i.getName(), self.getNodesLen())
            if i.getNodesLen() > 0:
                children = i.getNodes()
                if children is None:
                    res.append([i])
                else:
                    res.append([i, children])

        return res

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getNodesLen(self):
        return len(self.nodes)
