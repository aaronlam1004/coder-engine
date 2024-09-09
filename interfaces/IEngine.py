from abc import ABCMeta, ABC, abstractmethod
from typing import Tuple

class IEngine(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def Run(self, input_file: str) -> None:
        pass
