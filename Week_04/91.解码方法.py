#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        length=len(s)
        if length==0 or s[0]=='0':
            return 0
        f=[0]*length
        f[0]=1
        for i in range(1,length):
            if s[i]!='0':
                f[i]+=f[i-1]
            if '10'<=s[i-1:i+1]<='26':
                if i==1:
                    f[i]+=1
                else :
                    f[i]+=f[i-2]
        return f[-1]
        
# @lc code=end

