#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        num=0
        g1=s1=0
        while s1<len(s) and g1<len(g):
            if s[s1]>=g[g1]:
                num+=1
                g1+=1
            s1+=1
        return num

        
# @lc code=end

