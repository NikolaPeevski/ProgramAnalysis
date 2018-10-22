from typing import List

from types.Operator import Operator


class MathOperator(Operator):
    def available_operators(self) -> List[str]:
        return ['+', '-', '*', '/', '%']
