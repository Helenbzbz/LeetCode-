
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        num_set = set(nums)
        
        for num in num_set:
            if num-1 not in num_set:
                current_length = 1
                current_num = num
                
                while current_num+1 in num_set:
                    current_num += 1
                    current_length += 1
                    
                length = max(current_length, length)
                    
        return length
