from abc import ABCMeta, ABC, abstractmethod

class ISolution(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, solution_file: str, run_file: str):
        self.solution_file = solution_file
        self.run_file = run_file

    @abstractmethod
    def GenerateSolution(self) -> str:
        pass

    @abstractmethod
    def GenerateMain(self) -> str:
        pass

    @abstractmethod
    def Export(self) -> None:
        pass
