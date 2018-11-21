from abc import ABC


class Statement(ABC):
    # TODO Implement this
    def __init__(self, name: str, _type: str, *statement):
        self.name = name
        self.type = _type

        if statement is not None:
            self.statement = statement

    def getName(self):
        return self.name

    def getType(self):
        return self.type

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

