import os
import sys

FILE_PATH = os.path.dirname(__file__)
HOME_PATH = os.path.join(FILE_PATH, "..")

sys.path.append(HOME_PATH)
sys.path.append(os.path.join(HOME_PATH, "py"))

def GetTestSolutionFile(solution_filename: str) -> str:
    return os.path.join(FILE_PATH, solution_filename)

def GetTestRunFile(problem_name: str, run_filename: str) -> str:
    return os.path.join(HOME_PATH, "problems", problem_name, run_filename)

def GetTestCaseFile(case_filename: str) -> str:
    return os.path.join(FILE_PATH, "cases", case_filename)
