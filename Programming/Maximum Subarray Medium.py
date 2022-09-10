# This is n^2 we can have a quicker one
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_subarray = -math.inf
#         for i in range(len(nums)):
#             current_subarray = 0
#             for j in range(i, len(nums)):
#                 current_subarray += nums[j]
#                 max_subarray = max(max_subarray, current_subarray)
#         return max_subarray
    

# Whenenevr do a maximum or minimum question, we can consider dynamic programming, by moving forward and decide what is worth keeping

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]
        for num in nums[1:]:
            current_subarray = max(num,current_subarray+num)
            max_subarray = max(max_subarray,current_subarray)
        return max_subarray
        
