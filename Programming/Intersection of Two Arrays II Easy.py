class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_hash = {}
        for num in nums1:
            if num in num_hash:
                num_hash[num] = num_hash[num]+1
            else: num_hash[num] = 1
        over_lap = []
        for num in nums2:
            if num in num_hash:
                if num_hash[num] != 0: 
                    num_hash[num] = num_hash[num]-1
                    over_lap.append(num)
                else: del num_hash[num]
        return over_lap

# Idea 2: We can also use sort simplify to search process
# Idea 3: use the intersection built-in function in C => but in Python only set has this function, after turning it into sets, we loose miltiple appearance of one item
