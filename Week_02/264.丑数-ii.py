#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly=[1]
        p1=p2=p3=0
        while n>1:
            ugly_new=min(ugly[p1]*2,ugly[p2]*3,ugly[p3]*5)
            ugly.append(ugly_new)
            if ugly_new==ugly[p1]*2:
                p1+=1
            if ugly_new==ugly[p2]*3:
                p2+=1
            if ugly_new==ugly[p3]*5:
                p3+=1
            n-=1
        return ugly[-1]
# @lc code=end

