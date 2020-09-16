#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums,0,len(nums)-1)
    def mergeSort(self,nums,left,right):
        if left>=right:
            return 0
        mid=(left+right)>>1
        cnt=self.mergeSort(nums,left,mid)+self.mergeSort(nums,mid+1,right)
        j=mid+1
        for i in range(left,mid+1):
            while j<= right and nums[i]/2.0>nums[j]:
                j+=1
            cnt+=(j-mid-1)
        nums[left:right+1] = sorted(nums[left:right+1])
        #self.Merge(nums,left,mid,right)
        return cnt
# @lc code=end

