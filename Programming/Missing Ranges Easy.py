class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ## This takes high and low and format it into the correct way
        def format(lower, high):
            if lower == high: return str(lower)
            return str(lower) + '->' + str(high)
        
        ## initialize the prev as lowerbound-1
        result = []
        prev = lower-1
        for i in range(len(nums)+1):
            ## If curr in nums the num else upperbound+1
            curr = nums[i] if i < len(nums) else upper+1
            ## As soon as the last checkpoint +1 equal or smaller than next pointer -1 means there is at least 1 missing num in middle
            if prev+1 <= curr-1:
                result.append(format(prev+1,curr-1))
            ## Move the second pointer
            prev=curr
        return result
