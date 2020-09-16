#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        d=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    d[i]=max(d[i],d[j]+1)
        return max(d)
                    
# @lc code=end

