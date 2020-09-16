#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=0:
            return 0
        pre=0
        cur=1
        for i in range(n):
            tmp=cur
            cur=tmp+pre
            pre=tmp
        return cur
# @lc code=end

