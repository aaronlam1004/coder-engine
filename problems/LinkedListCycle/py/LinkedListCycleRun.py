from dataclasses import dataclass
from typing import *

from lib.ListNode import ListNode

from solution import Solution

@dataclass
class Args:
    head: ListNode
    result: List[int]

def ProcessInput(input_file: str) -> Args:
    lines = []
    with open(input_file, 'r') as inputs:
        lines = inputs.read().split('\n')

    nodes = lines[0].split(',')
    
    head = None
    prev = None
    node_list = []
    for i, val in enumerate(nodes):
        node = ListNode(int(val))
        if head is None:
            head = node
            prev = head
        else:
            prev.next = node
            prev = node
        node_list.append(node)

    pos = int(lines[1])
    if pos != -1:
        node_list[-1].next = node_list[pos]

    result = lines[2] == "true"
    args = Args(head, result)
    return args

def Run(args: Args) -> bool:
    print(Solution().hasCycle(args.head))
    return Solution().hasCycle(args.head) == args.result

