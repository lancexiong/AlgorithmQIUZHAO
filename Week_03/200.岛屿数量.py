#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.n,self.m=len(grid),len(grid[0])
        count=0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j]=='1':
                    count+=1
                    self.dfs(grid,i,j)
        return count
    def dfs(self,grid,row,col):
        if row>=self.n or col>=self.m or row<0 or col<0 or grid[row][col]!='1':
            return
        grid[row][col]='0'   
        self.dfs(grid,row-1,col)
        self.dfs(grid,row,col+1)
        self.dfs(grid,row+1,col)
        self.dfs(grid,row,col-1)
            
            
# @lc code=end

