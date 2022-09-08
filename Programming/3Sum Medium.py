## This solution won't work as it will always time out
## Maximum two loop
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         for i in range(0, len(nums)-2):
#             for j in range (i+1, len(nums)-1):
#                 for k in range (j+1, len(nums)):
#                     a = nums[i]
#                     b = nums[j]
#                     c = nums[k]
#                     if a+b+c == 0:
#                         row = [a,b,c]
#                         row.sort()
#                         if row not in result: result.append(row)                 
#         return result


# The two pointer method works in this way, sort the array from lower to higher. If the first one is bigger than 0, just return 0; if it is smaller than 0, trigger a second function
# The seocnd function will have two pointers, moving from start and from end, if the sum is bigger than 0, we well move the high point to left
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] > 0: 
                return result
            if i==0 or nums[i-1]!=nums[i]:
                lo, hi = i+1, len(nums)-1
                while lo<hi: 
                    sum = nums[i]+nums[lo]+nums[hi]
                    if sum<0: 
                        lo+=1
                    elif sum >0: 
                        hi-=1
                    else:
                        result.append([nums[i],nums[lo],nums[hi]])
                        lo +=1
                        hi -=1
                        while lo < hi and nums[lo] == nums[lo-1]:
                            lo+=1           
        return result
