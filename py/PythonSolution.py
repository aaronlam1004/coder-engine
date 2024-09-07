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
        py_code = "from typing import *\n"
        py_code += "import sys\n\n"
        lib_path = os.path.join(os.path.dirname(__file__), "lib")
        py_code += f"sys.path.append(\"{lib_path}\")\n\n".replace("\\", "\\\\")
        py_code += f"from ListNode import ListNode\n\n"

        if os.path.exists(self.solution_file):
            with open(self.solution_file, 'r') as py_file:
                py_code += py_file.read()

        # for import_file in imports:
        #     print(import_file)

        return py_code

    @override
    def Export(self) -> str:
        code = self.Generate()
        solution_file = os.path.join("build", os.path.basename(self.solution_file))
        with open(solution_file, 'w') as solution:
            solution.write(code)
        return solution_file
