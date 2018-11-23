from abc import ABC
from microCTypes.baseNode import baseNode


class Statement(baseNode):

    def __init__(self, name: str, _type):
        super().__init__(name, _type, None)

    def getSubStatement(self):
        return self.statement

    def expand(self):
        statements = []
        st = self.getSubStatement()

        while True:
            if isinstance(st, tuple):
                break
            else:
                statements.append(st)
            st = st.getSubStatement()

        return statements


