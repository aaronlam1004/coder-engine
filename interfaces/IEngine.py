from abc import ABCMeta, ABC, abstractmethod
from typing import Tuple

class IEngine(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, solution: str, solution_call: str):
        self.solution = solution
        self.solution_call = solution_call

    @abstractmethod
    def Run(self, expected: any, args: Tuple[any] = ()) -> None:
        pass
