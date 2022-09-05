## The function nums1 has length m+n m-> should be merged & n comes from nums 2
## Intuition -> put nums2 inside nums1 first and sort
## Another though -> 2 pointers, compare and insert from beginning
## Interview tips: everytime, 2 arrays merge, we can do 3 pointers from the end:
## one pointer at len(nums1) - m & at n in nums 2 and have one at the end
## two last numbers -> which one is bigger move to the end. Through comparing we fill in the array 1 one by one

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_p = m-1
        nums2_p = n-1
        nums1_copy = nums1.copy()
        
        for i in reversed(range(0,m+n)):
            
            if nums2_p == -1: 
                num2 = -999
                num1 = nums1_copy[nums1_p]
            elif nums1_p == -1: 
                num1 = -999
                num2 = nums2[nums2_p]
            else:
                num1 = nums1_copy[nums1_p]
                num2 = nums2[nums2_p]
            
            
            if num1 >= num2:
                nums1[i] = num1
                nums1_p = nums1_p-1
            else:
                nums1[i] = num2
                nums2_p = nums2_p-1

## Use the while it also solves the -1 issue I met
## Do not use save n-1 as a number to loop, this will have the -1 issue, instead use n-1 as the index to loop through
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        last = m + n -1
        
        while m > 0 and n> 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
            
        while n > 0:
            nums1[last] = nums2[n-1]
            last , n = last -1 , n - 1
