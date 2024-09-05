import os
import sys
from typing import override

sys.path.append("..")

from interfaces.ISolution import ISolution

class PythonSolution(ISolution):
    @override
    def __init__(self, solution_file: str, solution_call: str):
        super().__init__(solution_file, solution_call)

    @override
    def Generate(self) -> str:
        py_code = ""
        if os.path.exists(self.solution_file):
            with open(self.solution_file, 'r') as py_file:
                py_code = py_file.read()
        py_code = "from typing import List\n" + py_code
        return py_code

    @override
    def Export(self) -> str:
        code = self.Generate()
        solution_file = os.path.join("build", os.path.basename(self.solution_file))
        with open(solution_file, 'w') as solution:
            solution.write(code)
        return solution_file
