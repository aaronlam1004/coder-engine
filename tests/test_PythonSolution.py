import pytest

from TestUtils import *

from CoderEngine import CoderEngine

from PythonSolution import PythonSolution
from PythonEngine import PythonEngine

def test_PythonSolutions_CanBuildAndRun_ValidSolution():
    engine = CoderEngine(PythonSolution, PythonEngine, GetTestSolutionFile("py/TwoSumII.py"), GetTestRunFile("TwoSumII", "TwoSumIIRun.py"), cases = [GetTestCaseFile("case_TwoSumII.txt")])
    engine.Compile()
    assert engine.Run() == True

def test_PythonSolutions_CanBuildAndRun_InvalidSolution():
    engine = CoderEngine(PythonSolution, PythonEngine, GetTestSolutionFile("py/TwoSumIIInvalid.py"), GetTestRunFile("TwoSumII", "TwoSumIIRun.py"), cases = [GetTestCaseFile("case_TwoSumII.txt")])
    engine.Compile()
    assert engine.Run() == False

def test_PythonSolutions_CanBuildAndRun_ListNode_ValidSolution():
    engine = CoderEngine(PythonSolution, PythonEngine, GetTestSolutionFile("py/LinkedListCycle.py"), GetTestRunFile("LinkedListCycle", "LinkedListCycleRun.py"), modules = ["ListNode"], cases = [GetTestCaseFile("case_LinkedListCycle.txt")])
    engine.Compile()
    assert engine.Run() == True

def test_PythonSolutions_CanBuildAndRun_ListNode_InvalidSolution():
    engine = CoderEngine(PythonSolution, PythonEngine, GetTestSolutionFile("py/LinkedListCycleInvalid.py"), GetTestRunFile("LinkedListCycle", "LinkedListCycleRun.py"), modules = ["ListNode"], cases = [GetTestCaseFile("case_LinkedListCycle.txt")])
    engine.Compile()
    assert engine.Run() == False
