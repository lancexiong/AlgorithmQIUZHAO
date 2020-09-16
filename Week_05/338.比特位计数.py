#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans=[0]*(num+1)
        for i in range(1,num+1):
            ans[i]=ans[i & (i-1)]+1
        return ans
        
# @lc code=end

