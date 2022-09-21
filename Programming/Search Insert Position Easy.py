class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index in range(len(nums)):
            if nums[index] == target: return index
            if nums[index] > target and (index == 0 or nums[index-1] < target): return index
        return len(nums)
