from abc import ABCMeta, ABC, abstractmethod

class ISolution(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, solution_file: str, solution_call: str):
        self.solution_file = solution_file
        self.solution_call = solution_call

    @abstractmethod
    def Generate(self) -> str:
        pass

    @abstractmethod
    def Export(self, directory: str = '.') -> str:
        pass
