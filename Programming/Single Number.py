# Linear complexity is O(n) which will only allow one loop; we can't use sort -> its time complexity is O(n*logn) -> we can use hashmap though; 
# set is a way to remove all duplicates

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         i = 0
#         while i< len(nums)-1:
#             if nums[i] == nums[i+1]: i+=2
#             else: return nums[i]
#         return nums[-1]
    
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)
