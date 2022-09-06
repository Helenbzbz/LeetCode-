# My intuition thought is to do a scan one by one -> for each land, we start to test the surrounding 4 conditions -> This has to be a loop by loop index
# It's not right, island is not a single '1', it's a combination of multiple '1's on the map as soon as the whole piece has water around it => so we need something to store the data so that we won't search repeatly

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    total_count += 1
                    self.island_marker(i,j,grid)
        return total_count

    def island_marker (self, i, j, grid):
        if i <0 or j<0 or i == len(grid) or j== len(grid[0]) or grid[i][j] != '1':
            return
        else:
            grid[i][j] = '0' 
# Mark this to 0 so that after this scan all this island will be taken as water
        self.island_marker(i,j+1,grid)
        self.island_marker(i,j-1,grid)
        self.island_marker(i+1,j,grid)
        self.island_marker(i-1,j,grid)   
