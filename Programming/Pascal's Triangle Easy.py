# This question's time complexity has to be O(n^2), we have to loop through 2 iterations ... :(

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        prerow = [1,1]
        newrow = []
        i = 0
        while i < numRows-1:
            i = i+1
            newrow.append(1)
            for n in range(0,len(prerow)-1):
                newrow.append(prerow[n]+prerow[n+1])
            newrow.append(1)
            result.append(prerow)
            prerow = newrow
            newrow = []
        return result
