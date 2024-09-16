import os

import pytest

from TestUtils import FILE_PATH

from ProblemParser import ProblemParser

parser = ProblemParser()

def test_ProblemParser_CanParseValidProblem():
    problem_json_path = os.path.join(FILE_PATH, "problems", "TwoSumII", "TwoSumII.json")
    assert parser.GetProblem(problem_json_path) is not None

def test_ProblemParser_InvalidParse_NoName():
    problem_json_path = os.path.join(FILE_PATH, "problems", "InvalidJSONs", "ProblemNoName.json")
    assert parser.GetProblem(problem_json_path) is None

def test_ProblemParser_InvalidParse_NoDescription():
    problem_json_path = os.path.join(FILE_PATH, "problems", "InvalidJSONs", "ProblemNoDescription.json")
    assert parser.GetProblem(problem_json_path) is None

def test_ProblemParser_InvalidParse_NoLanguages():
    problem_json_path = os.path.join(FILE_PATH, "problems", "InvalidJSONs", "ProblemNoLanguages.json")
    assert parser.GetProblem(problem_json_path) is None

def test_ProblemParser_InvalidParse_NoLanguage():
    problem_json_path = os.path.join(FILE_PATH, "problems", "InvalidJSONs", "ProblemNoLanguage.json")
    assert parser.GetProblem(problem_json_path) is None

def test_ProblemParser_InvalidParse_UnsupportedLanguage():
    problem_json_path = os.path.join(FILE_PATH, "problems", "InvalidJSONs", "ProblemUnsupportedLanguage.json")
    assert parser.GetProblem(problem_json_path) is None

def test_ProblemParser_InvalidParse_NoRunner():
    problem_json_path = os.path.join(FILE_PATH, "problems", "InvalidJSONs", "ProblemNoRunner.json")
    assert parser.GetProblem(problem_json_path) is None

def test_ProblemParser_InvalidParse_NoRunner():
    problem_json_path = os.path.join(FILE_PATH, "problems", "InvalidJSONs", "ProblemNoModules.json")
    assert parser.GetProblem(problem_json_path) is None

def test_ProblemParser_InvalidParse_NoTemplate():
    problem_json_path = os.path.join(FILE_PATH, "problems", "InvalidJSONs", "ProblemNoModules.json")
    assert parser.GetProblem(problem_json_path) is None

def test_ProblemParser_InvalidParse_NoDescriptionFile():
    problem_json_path = os.path.join(FILE_PATH, "problems", "InvalidNoDescriptionFile", "TwoSumII.json")
    assert parser.GetProblem(problem_json_path) is None

def test_ProblemParser_InvalidParse_NoCaseFolder():
    problem_json_path = os.path.join(FILE_PATH, "problems", "InvalidNoCaseFolder", "TwoSumII.json")
    assert parser.GetProblem(problem_json_path) is None

def test_ProblemParser_InvalidParse_NoLanguageFolder():
    problem_json_path = os.path.join(FILE_PATH, "problems", "InvalidNoLanguage", "TwoSumII.json")
    assert parser.GetProblem(problem_json_path) is None

def test_ProblemParser_InvalidParse_NoRunnerFile():
    problem_json_path = os.path.join(FILE_PATH, "problems", "InvalidNoRunnerFile", "TwoSumII.json")
    assert parser.GetProblem(problem_json_path) is None

def test_ProblemParser_InvalidParse_NoTemplateFile():
    problem_json_path = os.path.join(FILE_PATH, "problems", "InvalidNoTemplateFile", "TwoSumII.json")
    assert parser.GetProblem(problem_json_path) is None
