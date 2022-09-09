# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         if len(nums) == 1: return nums[0]
#         hashset = {}
#         for num in nums:
#             if num in hashset.keys(): 
#                 if hashset[num] + 1 > len(nums)/2: return num
#                 else: hashset[num] = hashset[num]+1
#             else: 
#                 hashset[num] = 1
                
# Sort has time complexity of n
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        nums.sort()
        return nums[floor((len(nums)/2))]
