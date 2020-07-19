# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 18:06:29 2020

@author: MyPC
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums_copy=nums1[:m]
        nums1[:]=[]
        p1=p2=0
        while p1<m and p2<n:
            if nums_copy[p1]<=nums2[p2]:
                nums1.append(nums_copy[p1])
                p1+=1
            else:
                nums1.append(nums2[p2])
                p2+=1
        if p1<m:
            nums1[p1+p2:]=nums_copy[p1:]
        if p2<n:
            nums1[p1+p2:]=nums2[p2:]