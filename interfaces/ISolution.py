from typing import List
from abc import ABCMeta, ABC, abstractmethod

class ISolution(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, solution_file: str, run_file: str, modules: List[str] = []):
        self.solution_file = solution_file
        self.run_file = run_file
        self.modules = modules 

    @abstractmethod
    def GenerateSolution(self) -> str:
        pass

    @abstractmethod
    def GenerateMain(self) -> str:
        pass

    @abstractmethod
    def Compile(self) -> None:
        pass
