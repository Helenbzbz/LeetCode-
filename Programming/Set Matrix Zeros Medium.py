# My intuitional solution is to store everything in a set with row and column number and then when we find anything 0, we will start from there and change the element with same row or column to 0
# smarter choice to set first cell of every row and column as flag if cell[i][j] == 0 then cell[i][0] = 0 and cell[0][j] = 0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        is_column = False
        # This is because the first cell can only represent one thing, we choose to let it represent the row, it can't represent the column then
        
        for i in range(R):
            if matrix[i][0] == 0: is_column = True
            for j in range(1,C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # Start to scan the row below row 1 & column below column 1
        for i in range(1,R):
            for j in range(1,C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Start to scan row 1
        if matrix[0][0] == 0:
            for j in range(C):
                  matrix[0][j] = 0
        
        # Start to scan column 1
        if is_column:
            for i in range(R):
                  matrix[i][0] = 0
