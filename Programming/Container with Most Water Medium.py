# As each time we move, we loose at least 1* left or right, therefore we should move inward the one that is shorter so that the gain can outweights the loss
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        area = 0
        
        while i<j:
            width = j-i
            area = max(area, min(height[i],height[j])*width)
            if height[i] <= height[j]: i+=1
            elif height[i] > height[j]: j-=1
                
        return area
