# This solution fails the time complexity, this one has O((m+n)log(m+n))
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums3 = nums1+nums2
#         nums3.sort()
#         nl = len(nums3)
#         if nl%2 == 0:
#             small = (nums3[int(nl/2)-1])
#             big = nums3[int(nl/2)]
#             return (small+big)/2
#         else:
#             return nums3[floor(nl/2)]
        
# We know whenever there is a requirement for only log, we consider binary search
# We first do total_length/2 => then we get a number/2 again, find the corresponding item in each array => if left[3]< right[4] ok; if bigger, we have to adjust it by moving to left[2] and right[4]
# When it's odd, we take which one is bigger left[2+1] or right[4+1]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1)+len(nums2)
        half = total//2
        
        if len(B)<len(A):
            A,B = B,A
            
        l,r = 0, len(A)-1
        while True:
            i = (l+r)//2
            j = half-i-2
            
            Aleft = A[i] if i>=0 else float("-infinity")
            Aright = A[i+1] if i< len(A)-1 else float('infinity')
            Bleft = B[j] if j>=0 else float('-infinity')
            Bright = B[j+1] if i< len(B)-1 else float('infinity')
            
            if Aleft <= Bright and Bleft <= Aright:
                if total%2 ==1: return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright: 
                r = i-1
            else: l = i+1
