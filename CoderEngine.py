import os
from enum import Enum
from typing import *

from interfaces.ISolution import ISolution
from interfaces.IEngine import IEngine

FILE_PATH = os.path.dirname(__file__)

from py.PythonSolution import PythonSolution
from py.PythonEngine import PythonEngine

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

    def Compile(self) -> None:
        self.solution.Compile()

    def Run(self) -> None:
        for case in self.cases:
            self.engine.Run(case)

if __name__ == '__main__':
    # Two Sum II
    # engine = CoderEngine(PythonSolution, PythonEngine, "TwoSumII.py", os.path.join("problems", "TwoSumII", "TwoSumIIRun.py"))
    # engine.Run()

    # Linked List Cycle
    engine = CoderEngine(PythonSolution, PythonEngine, "LinkedListCycle.py", os.path.join(FILE_PATH, "problems", "LinkedListCycle", "LinkedListCycleRun.py"), modules = ["ListNode"], cases = [os.path.join(FILE_PATH, "problems", "LinkedListCycle", "cases", "case1.txt")])
    engine.Compile()
    engine.Run()

