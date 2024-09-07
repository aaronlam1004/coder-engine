import os
import sys
import importlib
import time
from typing import Tuple, override

sys.path.append("..")

from interfaces.IEngine import IEngine 

class PythonEngine(IEngine):
    @override
    def __init__(self, solution: str, solution_call: str):
        super().__init__(solution, solution_call)

    @override
    def Run(self, expected: any, args: Tuple[any] = tuple()):
        if os.path.exists("build") and os.path.exists(os.path.join("build", f"{self.solution}.py")):
            start = time.time()
            solution_module = importlib.import_module(f"build.{self.solution}")
            solution = solution_module.Solution()
            call = getattr(solution, self.solution_call)
            result = call(*args) == expected
            process_time_ms = (time.time() - start) * 1000
            print(args, process_time_ms, result)
