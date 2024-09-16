from typing import Union, Dict, List
from enum import Enum
from dataclasses import dataclass
import json
import os

SUPPORTED_LANGUAGES = [
    "py"
]

class Runner:
    runner: str = ""
    modules: List[str] = []
    template: str = ""

    def Print(self) -> str:
        print("Runner:", self.runner)
        print("Modules:", self.modules)
        print("Template:", self.template)

    def FromJSON(self, runner_dict: Dict[str, any]) -> None:
        self.runner = runner_dict["runner"]
        self.modules = runner_dict["modules"]
        self.template = runner_dict["template"]

class Problem:
    name: str = ""
    description: str = ""
    cases: List[str] = []
    languages: Dict[str, Runner] = dict()

    def Print(self) -> str:
        print("Name:", self.name)
        print("Description:", self.description)
        print("Cases:", self.cases)
        print("Languages:")
        for language, runner in self.languages.items():
            print(f"= {language} =:")
            runner.Print()

    def FromJSON(self, problem_json: Dict[str, any]) -> None:
        self.name = problem_json["name"]
        self.description = problem_json["description"]
        self.cases = problem_json["cases"]
        for lang, runner_dict in problem_json["languages"].items():
            runner = Runner()
            runner.FromJSON(runner_dict)
            self.languages[lang] = runner

class ProblemParser:
    def GetProblemJSON(self, problem: str) -> Union[Dict[str, any], None]:
        if os.path.exists(problem) and problem.endswith(".json"):
            try:
                with open(problem, 'r') as problem_file:
                    problem_json = json.loads(problem_file.read())
                return problem_json
            except Exception as exception:
                return None
        return None

    def ValidateProblemJSON(self, problem_json: Dict[str, any], problem_path: str) -> bool:
        if "name" not in problem_json:
            print("Error - Problem has no \"name\"")
            return False

        if "description" not in problem_json:
            print("Error - Problem has no \"description\"")
            return False 
        if not os.path.exists(os.path.join(problem_path, problem_json["description"])):
            print(f"Error - Problem cannot find \"description\" file - {problem_json['description']}")
            return False
        problem_json["description"] = os.path.join(problem_path, problem_json["description"])

        if "cases" not in problem_json:
            print("Error - Problem has no \"cases\"")
            return False
        if not os.path.exists(os.path.join(problem_path, "cases")):
            print("Error - Problem cannot find folder \"cases\"")
            return False
        for i, case in enumerate(problem_json["cases"]):
            if not os.path.exists(os.path.join(problem_path, "cases", case)):
                print(f"Error - Problem cannot find \"description\" file - {case}")
                return False
            else:
                problem_json["cases"][i] = os.path.join(problem_path, "cases", case)

        if "languages" not in problem_json:
            print("Error - Problem has no \"languages\"")
            return False
        for lang, runner in problem_json["languages"].items():
            if lang not in SUPPORTED_LANGUAGES:
                print(f"Error - Problem does not support language - {lang}")
                return False
            if not os.path.exists(os.path.join(problem_path, lang)):
                print(f"Error - Problem cannot find folder \"{lang}\"")
                return False
            lang_path = os.path.join(problem_path, lang)

            if "runner" not in problem_json["languages"][lang]:
                print(f"Error - Problem ({lang}) has no \"runner\"")
                return False
            if not os.path.exists(os.path.join(lang_path, problem_json["languages"][lang]["runner"])):
                print(f"Error - Problem ({lang}) cannot find runner file - {problem_json['languages'][lang]['runner']}")
                return False
            problem_json["languages"][lang]["runner"] = os.path.join(lang_path, problem_json["languages"][lang]["runner"])

            if "modules" not in problem_json["languages"][lang]:
                print(f"Error - Problem ({lang}) has no \"modules\"")
                return False
            # TODO: check if modules exist

            if "template" not in problem_json["languages"][lang]:
                print(f"Error - Problem ({lang}) has no \"template\"")
                return False
            if not os.path.exists(os.path.join(lang_path, problem_json["languages"][lang]["template"])):
                print(f"Error - Problem ({lang}) cannot find template file - {problem_json['languages'][lang]['template']}")
                return False
            problem_json["languages"][lang]["template"] = os.path.join(lang_path, problem_json["languages"][lang]["template"])

        return True

    def GetProblem(self, problem_file: str) -> Problem:
        problem_json = self.GetProblemJSON(problem_file)
        if problem_json is not None:
            if self.ValidateProblemJSON(problem_json, os.path.abspath(os.path.dirname(problem_file))):
                problem = Problem()
                # problem.FromJSON(problem_json)
                problem.Print()
                return problem
        return None
