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
    def Run(self, expected: any, args: Tuple[any] = ()):
        if os.path.exists("build") and os.path.exists(os.path.join("build", f"{self.solution}.py")):
            start = time.time()
            solution = importlib.import_module(f"build.{self.solution}")
            args = ','.join([str(arg) for arg in args])
            result = eval(f"solution.Solution().{self.solution_call}({args}) == {expected}")
            process_time_ms = (time.time() - start) * 1000
            print(args, process_time_ms, result)
