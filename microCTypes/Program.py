from microCTypes.Declaration import Declaration
from microCTypes.Statement import Statement
from microCTypes.baseNode import baseNode
from microCTypes.WhileStatement import WhileStatement


class Program(baseNode):

    # TODO Implement this
    def __init__(self, name: str):
        super().__init__(name, "Base", None)

    def insertProgramEntry(self, node):
        super().appendNode(node)
        return node

    def toString(self):
        res = ""
        # innerBlockCounter = 0
        #
        # for i in range(len(self.programBlocks)):
        #     block = self.programBlocks[i]
        #
        #     # Could have special methods in the future
        #     if isinstance(block, Statement):
        #         res += '{} {}'.format(i + 1 + innerBlockCounter, self.programBlocks[i].getName())
        #
        #         innerStatements = self.programBlocks[i].expand()
        #
        #         for st_i in range(len(innerStatements)):
        #             innerBlockCounter += 1
        #             res += "\n"
        #             res += '{} {}'.format(i + 1 + innerBlockCounter, innerStatements[st_i].getName())
        #
        #     else:
        #         res += '{} {}'.format(i + 1 + innerBlockCounter, self.programBlocks[i].getName())
        #
        #     res += "\n"

        return res

    def getProgramBlocks(self):
        res = []

        baseLevelNodes = super().getNodes()

        print(baseLevelNodes)
