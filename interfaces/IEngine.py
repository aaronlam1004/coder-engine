from abc import ABCMeta, ABC, abstractmethod
from typing import Tuple

class IEngine(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def Run(self) -> None:
        pass
