class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
        row = len(board)
        column = len(board[0])
        
        def get_neighbor(r,c,row,column,matrix):
            total_lives = 0
            for neighbor in neighbors:
                r_num = r+neighbor[0]
                c_num = c+neighbor[1]
                
                if r_num >= 0 and r_num < row and c_num >= 0 and c_num < column:
                    if matrix[r_num][c_num] == 1 or matrix[r_num][c_num] == -1:
                        total_lives += 1
            return total_lives
                
        for r in range(0,row):
            for c in range(0,column):
                total_lives = get_neighbor(r,c,row,column,board)
                if board[r][c] == 1:
                    if total_lives < 2 or total_lives > 3:
                        board[r][c] = -1
                else:
                    if total_lives == 3:
                        board[r][c] = 2
        
        for r in range(row):
            for c in range(column):
                if board[r][c] == -1: board[r][c] = 0
                if board[r][c] == 2: board[r][c] = 1
