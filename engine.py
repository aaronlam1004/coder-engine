import os
from enum import Enum

from interfaces.ISolution import ISolution
from interfaces.IEngine import IEngine

from py.solution import PythonSolution
from py.engine import PythonEngine

class CoderLanguage(Enum):
    PYTHON = "PYTHON"

class CoderEngine:
    def __init__(self, solution: ISolution, engine: IEngine, solution_file: str, solution_call: str):
        self.solution = solution(solution_file, solution_call)
        module = os.path.splitext(os.path.basename(solution_file))[0]
        self.engine = engine(module, solution_call)

        if not os.path.exists("build"):
            os.makedirs("build", exist_ok=True)

    def Run(self) -> None:
        self.solution.Export()
        self.engine.Run([1, 2], args = ([2, 7, 11, 15], 9))

if __name__ == '__main__':
    engine = CoderEngine(PythonSolution, PythonEngine, "TwoSumII.py", "twoSum")
    engine.Run()


