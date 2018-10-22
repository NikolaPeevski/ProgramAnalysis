from typing import List

from types.Statement import Statement


class StatementSequence:

    def __init__(self, statements: List[Statement] = []):
        self.statements = statements

    def add_statement(self, statement: Statement) -> None:
        self.statements.append(statement)

    def get_statements(self) -> List[Statement]:
        return self.statements
