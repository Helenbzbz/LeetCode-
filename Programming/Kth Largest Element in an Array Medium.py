# # This will time out
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         largest_k = []
#         for num in nums:
#             if len(largest_k) >= k: 
#                 largest_k.sort()
#                 if num>largest_k[0]: largest_k[0] = num
#             else: largest_k.append(num)
#         largest_k.sort()
#         return largest_k[0]
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k,nums)[-1]
