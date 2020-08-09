#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        if n<=1:
            return 0
        '''
        f[i]:第i个字符结尾的最长有效括号数
        if s[i]=')' and s[i-1]='(' 则f[i]=f[i-2]+2
        if s[i]=')' and s[i-1]=')'  and s[i-f[i-1]-1]='(' 则f[i]=f[i-1]+f[i-f[i-1]-2]+2
        '''
        f=[0]*n
        for i in range(1,n):
            if s[i]==')' and s[i-1]=='(':
                f[i]=2+(f[i-2] if i>=2 else 0)
            elif s[i]==')' and s[i-1]==')' :
                if i>=f[i-1]+1 and s[i-f[i-1]-1]=='(':
                    f[i]=f[i-1]+(f[i-f[i-1]-2] if i>=f[i-1]+2 else 0)+2
        return max(f)
                
# @lc code=end

