# this is by looping through the supposed range and check in it's in the list
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         for i in range(0, len(nums)+1):
#             if i not in nums: return i
            
# For number question we can always think about mathematical solution, it usually has O(1) instead of O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = len(nums)
        return int(((0+a)/2)*(a+1) - sum(nums))
