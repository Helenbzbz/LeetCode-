# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# The way I'm thinking is to use hashtable this has time complexity of O(m+n) and space of O(m+n)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_hash = set()
        while headA is not None:
            a_hash.add(headA)
            headA = headA.next
        while headB is not None:
            if headB in a_hash: return headB
            headB = headB.next
        return None


# A better way is to use pointers -> remember when trying to find something, it's always better to consider pointers instead of hashtable; We have two pointers, one is pointer a and one is pointer b; we can have one pointer goes over a+c+b and b+c+a => measuring long_distance and short_distance

# These two pointer, when a+c finished, b will also finished and start from a => two start with equal remaining lengths

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa = headA
        pb = headB
        while pa!=pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa
