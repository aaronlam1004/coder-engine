import pytest

from TestUtils import GetTestSolutionFile, GetPyRunFile, GetTestCaseFile

from CoderEngine import CoderEngine

from PythonSolution import PythonSolution
from PythonEngine import PythonEngine

def test_PythonSolutions_CanBuildAndRun_ValidSolution():
    engine = CoderEngine(PythonSolution, PythonEngine, GetTestSolutionFile("py/TwoSumII.py"), GetPyRunFile("TwoSumII", "TwoSumIIRun.py"), cases = [GetTestCaseFile("TwoSumII", "case1.txt")])
    engine.Compile()
    assert engine.Run() == True

def test_PythonSolutions_CanBuildAndRun_InvalidSolution():
    engine = CoderEngine(PythonSolution, PythonEngine, GetTestSolutionFile("py/TwoSumIIInvalid.py"), GetPyRunFile("TwoSumII", "TwoSumIIRun.py"), cases = [GetTestCaseFile("TwoSumII", "case1.txt")])
    engine.Compile()
    assert engine.Run() == False

def test_PythonSolutions_CanBuildAndRun_ListNode_ValidSolution():
    engine = CoderEngine(PythonSolution, PythonEngine, GetTestSolutionFile("py/LinkedListCycle.py"), GetPyRunFile("LinkedListCycle", "LinkedListCycleRun.py"), modules = ["ListNode"], cases = [GetTestCaseFile("LinkedListCycle", "case1.txt")])
    engine.Compile()
    assert engine.Run() == True

def test_PythonSolutions_CanBuildAndRun_ListNode_InvalidSolution():
    engine = CoderEngine(PythonSolution, PythonEngine, GetTestSolutionFile("py/LinkedListCycleInvalid.py"), GetPyRunFile("LinkedListCycle", "LinkedListCycleRun.py"), modules = ["ListNode"], cases = [GetTestCaseFile("LinkedListCycle", "case1.txt")])
    engine.Compile()
    assert engine.Run() == False
