class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        store = []
        index = 0
        i = 0
        while i <len(nums):
            num = nums[i]
            if num in store:
                del nums[i]
            else:
                store.append(num)
                i += 1    
        return len(nums)
             
# A better two pointer solution, check if right = left
# When they are not equal, the right will become the left
