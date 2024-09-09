import os
import sys
import shutil
from typing import *

HOME_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(HOME_PATH)

from interfaces.ISolution import ISolution

class PythonSolution(ISolution):
    @override
    def __init__(self, solution_file: str, run_file: str, modules: List[str] = []):
        super().__init__(solution_file, run_file, modules)

    @override
    def GenerateSolution(self) -> str:
        py_code = "from typing import *\n"
        py_code += "import os\n"
        py_code += "import sys\n\n"

        lib_path = os.path.join(os.path.dirname(__file__), "lib")
        shutil.copytree(lib_path, os.path.join(HOME_PATH, "build", "lib"), dirs_exist_ok=True)

        for module in self.modules:
            py_code += f"from lib.{module} import {module}\n"

        if len(self.modules) > 0:
            py_code += "\n"

        if os.path.exists(self.solution_file):
            with open(self.solution_file, 'r') as py_file:
                py_code += py_file.read()

        return py_code

    @override
    def GenerateMain(self) -> str:
        main_code = ""
        main_file = os.path.join(os.path.dirname(__file__), "main.py")
        with open(main_file, 'r') as main:
            main_code = main.read()

        module = os.path.basename(self.run_file).split('.')[0]
        run_file = os.path.join(HOME_PATH, "build", f"{module}.py")
        shutil.copy(self.run_file, run_file)

        main_code = main_code.replace("# {{ RUN_IMPORT }}", f"from {module} import *")
        return main_code

    @override
    def Compile(self) -> None:
        solution_code = self.GenerateSolution()
        solution_file = os.path.join(HOME_PATH, "build", "solution.py")
        with open(solution_file, 'w') as solution:
            solution.write(solution_code)

        main_code = self.GenerateMain()
        main_file = os.path.join(HOME_PATH, "build", "main.py")
        with open(main_file, 'w') as main:
            main.write(main_code)
