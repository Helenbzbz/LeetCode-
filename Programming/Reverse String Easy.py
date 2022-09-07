class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        front = 0
        end = len(s)-1
        while front < end:
            endchar = s[end]
            s[end] = s[front]
            s[front] = endchar
            front += 1
            end -= 1
        return s
    
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s.reverse()
