# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 20:08:52 2020

@author: MyPC
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        nums[:]=nums[:i+1]