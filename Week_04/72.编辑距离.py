#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        d[i][j]:A的前i个字符与B的前j个字符的编辑距离
        if A的最后一个字符与B的最后一个字符相同，则d[i][j]=min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1])
        if A的最后一个字符与B的最后一个字符不同，则d[i][j]=min(d[i-1][j],d[i][j-1],d[i-1][j-1])+1
        '''
        n1,n2=len(word1),len(word2)
        d=[[0]*(n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            for j in range(n2+1):
                if i==0:
                    d[i][j]=j
                elif j==0:
                    d[i][j]=i
                elif word1[:i][-1]==word2[:j][-1]:
                    d[i][j]=min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1])
                else:
                    d[i][j]=min(d[i-1][j],d[i][j-1],d[i-1][j-1])+1
        return d[n1][n2]
# @lc code=end

