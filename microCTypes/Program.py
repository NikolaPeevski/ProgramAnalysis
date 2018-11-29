from microCTypes.BaseNode import BaseNode


class Program(BaseNode):

    # TODO Implement toString
    #
    def __init__(self, name: str):
        super().__init__(name, "Base", None)

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

        baseLevelNodes = super().getNodes(0)

        # print(baseLevelNodes)
