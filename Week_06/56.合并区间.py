#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_new=sorted(intervals,key=lambda x: x[0])
        res=[]
        for inter in intervals_new:
            if len(res)==0 or res[-1][1]<inter[0]:
                res.append(inter)
            else:
                res[-1][1]=max(res[-1][1],inter[1])
        return res
# @lc code=end

