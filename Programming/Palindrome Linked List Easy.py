# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# My first thought is to read it into an array and then sort it reversly to see if they are euqal
# Another thought is to do pointer but since it is liked list I think the first method is slightly better?

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        array.append(head.val)
        while (head.next != None):
            head = head.next
            array.append(head.val)         
        l = 0
        r = len(array)-1
        while l < r:
            if array[l] != array[r]:
                return False
            else:
                l+=1
                r-=1    
        return True

# However, all the above solution doesn't give a O(1) space -> in order to do a O(1) space, runtime stack everytime when a function is called within a function, have to keep track of local variable => we reverse the second half of lnked list and comparing with the first half

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        
        # Check whether or not it's a palindrome
        result = True
        while result and second_half_start is not None:
            if head.val != second_half_start.val:
                result = False
            head = head.next
            second_half_start = second_half_start.next
        return result
        
# Find the end of first half and reverse second (we have two pointer, one is moving twice quickly as the first one)
        
    def end_of_first_half (self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse_list (self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
        
