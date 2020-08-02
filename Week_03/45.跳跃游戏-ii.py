#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        maxpostion,end,step=0,0,0
        for i in range(len(nums)-1):
            if maxpostion>=i:
                maxpostion=max(maxpostion,i+nums[i])
                if i==end:
                    end=maxpostion
                    step+=1
        return step
# @lc code=end

