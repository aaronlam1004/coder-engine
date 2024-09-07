# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = {}
        while head != None:
            if head in nodes and nodes[head]:
                return True
            nodes[head] = True
            head = head.next
        return False
