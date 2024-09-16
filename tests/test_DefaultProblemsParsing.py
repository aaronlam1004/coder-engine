import os

import pytest

from TestUtils import HOME_PATH

from ProblemParser import ProblemParser

parser = ProblemParser()

def test_ProblemParser_CanParseTwoSumII():
    problem_json_path = os.path.join(HOME_PATH, "problems", "TwoSumII", "TwoSumII.json")
    assert parser.GetProblem(problem_json_path) is not None

def test_ProblemParser_CanParseLinkedListCycle():
    problem_json_path = os.path.join(HOME_PATH, "problems", "LinkedListCycle", "LinkedListCycle.json")
    print(problem_json_path)
    assert parser.GetProblem(problem_json_path) is not None
