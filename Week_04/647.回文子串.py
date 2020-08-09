#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        d=[[0]*n for _ in range(n)]
        cnt=0
        for i in range(n-1,-1,-1):
            for j in range(n-1,i-1,-1):
                if s[i]==s[j] and (j-i<=2 or d[i+1][j-1]):
                    d[i][j]=1
                    cnt+=1
                else:
                    d[i][j]=0
        return cnt
                
        
# @lc code=end

