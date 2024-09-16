from dataclasses import dataclass
from typing import *

from solution import Solution

@dataclass
class Args:
    numbers: List[int]
    target: int
    result: List[int]

def ProcessInput(input_file: str) -> Args:
    lines = []
    with open(input_file, 'r') as inputs:
        lines = inputs.read().split('\n')
    numbers = [int(num) for num in lines[0].split(',')]
    target = int(lines[1])
    result = [int(index) for index in lines[2].split(',')]
    args = Args(numbers, target, result)
    return args

def Run(args: Args) -> bool:
    print(Solution().twoSum(args.numbers, args.target))
    return Solution().twoSum(args.numbers, args.target) == args.result

