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
    def Run(self):
        main = os.path.join(HOME_PATH, "build", "main.py")
        if os.path.exists(main):
            subprocess.call(f"python {main} problems/TwoSumII/cases/case1.txt", shell=True)
