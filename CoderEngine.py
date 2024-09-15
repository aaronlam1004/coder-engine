import os
from enum import Enum
from typing import *

from interfaces.ISolution import ISolution
from interfaces.IEngine import IEngine

FILE_PATH = os.path.dirname(__file__)

class CoderLanguage(Enum):
    PYTHON = "PYTHON"

class CoderEngine:
    def __init__(
        self,
        solution: ISolution,
        engine: IEngine,
        solution_file: str,
        run_file: str,
        cases: List[str] = [],
        modules: List[str] = [],
    ):
        self.solution = solution(solution_file, run_file, modules)
        self.engine = engine()
        self.cases = cases

        if not os.path.exists(os.path.join(FILE_PATH, "build")):
            os.makedirs(os.path.join(FILE_PATH, "build"), exist_ok=True)

    def ChangeEngine(self, engine: IEngine) -> None:
        self.engine = engine

    def ChangeSolution(self, solution: ISolution) -> None:
        self.solution = solution

    def Compile(self) -> None:
        self.solution.Compile()

    def Run(self) -> bool:
        result = True
        for case in self.cases:
            result &= self.engine.Run(case)
        return result
