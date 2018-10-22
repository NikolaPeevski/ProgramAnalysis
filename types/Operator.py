from abc import ABC, abstractmethod
from typing import List


class Operator(ABC):

    def __init__(self, operator: str):
        if self.valid_operator(operator):
            self.operator = operator

    @abstractmethod
    def available_operators(self) -> List[str]:
        return []

    def valid_operator(self, operator: str) -> bool:
        for op in self.available_operators():
            if op == operator:
                return True

        return False
