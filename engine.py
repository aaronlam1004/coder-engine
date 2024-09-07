import os
from enum import Enum

from interfaces.ISolution import ISolution
from interfaces.IEngine import IEngine

from py.PythonSolution import PythonSolution
from py.PythonEngine import PythonEngine

from py.lib.ListNode import ListNode

class CoderLanguage(Enum):
    PYTHON = "PYTHON"

class CoderEngine:
    def __init__(self, solution: ISolution, engine: IEngine, solution_file: str, solution_call: str):
        self.solution = solution(solution_file, solution_call)
        module = os.path.splitext(os.path.basename(solution_file))[0]
        self.engine = engine(module, solution_call)

        if not os.path.exists("build"):
            os.makedirs("build", exist_ok=True)

    def Run(self) -> None:
        self.solution.Export()
        # self.engine.Run([1, 2], args = ([2, 7, 11, 15], 9))
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next = ListNode(-4)
        head.next.next.next = head
        self.engine.Run(True, args = (head, ))

if __name__ == '__main__':
    # Two Sum II
    # engine = CoderEngine(PythonSolution, PythonEngine, "TwoSumII.py", "twoSum")
    # engine.Run()

    # Linked List Cycle
    engine = CoderEngine(PythonSolution, PythonEngine, "LinkedListCycle.py", "hasCycle")
    engine.Run()

