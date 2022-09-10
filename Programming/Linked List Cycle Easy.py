# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        appeared = set()
        while head.next != None and head not in appeared:
            appeared.add(head)
            head = head.next
        if head.next == None: return False
        else: return True
