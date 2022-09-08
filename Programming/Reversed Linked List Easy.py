# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = head ## Refer to the head
        prev = None
        while new:
            next_node = new.next ## copy the next_node
            new.next = prev ## change next node to previous one
            prev = new ## previous one will then be 
            new = next_node   
        return prev
