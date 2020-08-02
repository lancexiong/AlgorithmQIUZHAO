#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candidate=None
        for n in nums:
            if count==0:
                candidate=n
            count+= (1 if candidate==n else -1)
        return candidate    
        
# @lc code=end

