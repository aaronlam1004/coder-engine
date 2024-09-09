import os
import sys
import importlib
import time
from typing import Tuple, override
import subprocess

HOME_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(HOME_PATH)

from interfaces.IEngine import IEngine 

class PythonEngine(IEngine):
    @override
    def Run(self, input_file: str) -> bool:
        main = os.path.join(HOME_PATH, "build", "main.py")
        exit_code = subprocess.call(f"python {main} {input_file}", shell=True)
        print("Solution:")
        print(f"{input_file}: ", end='')
        if exit_code == 0:
            print("PASSED")
        else:
            print("FAILED")
        return exit_code == 0
