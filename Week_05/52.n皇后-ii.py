#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n<=0:
            return []
        self.cnt=0
        self.dfs(n,0,0,0,0)
        return self.cnt
    def dfs(self,n,row,col,pie,na):
        if row>=n:
            self.cnt+=1
            return 
        #bits=((~col) & (~pie) & (~na)) & ((1 << n)-1)
        bits=(~(col | pie | na)) & ((1 << n)-1)
        while bits:
            p=bits & (-bits)
            bits=bits & (bits-1)
            self.dfs(n,row+1,col | p,(pie | p) <<1,(na | p) >> 1)
        
# @lc code=end

