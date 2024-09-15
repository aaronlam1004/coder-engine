from typing import Union, Dict
import json
import os

PROBLEM_KEYS = [
    "name",
    "description",
    "cases"
    "languages",
]

RUNNER_KEYS = {
    "runner",
    "modules",
    "template",
}

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

    def ParseProblem(self, problem: str):
        problem_json = self.GetProblemJSON(problem)
        self.PrintProblemVerbose(problem_json)

    def PrintProblemVerbose(self, problem_json) -> None:
        print("Name:", problem_json["name"])
        print("Description:", problem_json["description"])
        print("Cases:", problem_json["cases"])
        print("Languages:", problem_json["languages"])

if __name__ == '__main__':
    parser = ProblemParser()
    parser.ParseProblem("./problems/TwoSumII/TwoSumII.json")
