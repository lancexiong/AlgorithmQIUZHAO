#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n,m=len(matrix),len(matrix[0])
        f=[[0]*m for _ in range(n)]
        Max=0
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    f[i][j]=int(matrix[i][j])
                elif matrix[i][j]=='0':
                    f[i][j]=0
                else:
                    f[i][j]=1+min(f[i-1][j-1],f[i][j-1],f[i-1][j])
                Max=max(Max,f[i][j])
        return Max*Max
# @lc code=end

