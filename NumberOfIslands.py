"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_islands = 0
        for i in range(len(grid)):
          for j in range(len(grid[i])):
            if grid[i][j] == "1":
              self.explode(grid,[i,j])
              num_islands +=1
        return num_islands
              
              
    
    
    def explode(self,grid,position):
        """
        :type grid: List[List[str]]
        :type position: List[int]
        """
        if position[0] < len(grid) and position[1]<len(grid[0]) and position[0]>=0 and position[1]>=0:

          if grid[position[0]][position[1]] == "1":
            grid[position[0]][position[1]] = "0"
            self.explode(grid, [position[0]+1,position[1]])
            self.explode(grid, [position[0]-1,position[1]])
            self.explode(grid, [position[0],position[1]+1])
            self.explode(grid, [position[0],position[1]-1])