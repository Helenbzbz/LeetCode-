class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0
        while count < len(nums):
            if nums[i] == 0: 
                nums.pop(i)
                nums.append(0)
            else: i+=1
            count +=1
