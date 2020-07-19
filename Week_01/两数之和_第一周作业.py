# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:17:50 2020

@author: MyPC
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        length=len(nums)
        for i in range(length):
            dic[nums[i]]=i
        for i in range(length):
            complement=target-nums[i]
            j=dic.get(complement)
            if j is not None and j!=i:
                return [i,j]