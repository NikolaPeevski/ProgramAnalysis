from typing import List

from types.Operator import Operator


class BinaryOperator(Operator):
    def available_operators(self) -> List[str]:
        return ['|', '&']
