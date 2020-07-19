# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 19:10:33 2020

@author: MyPC
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic1={}
        for i in range(len(s)):
            dic1[s[i]]=dic1.get(s[i],0)+1
            dic1[t[i]]=dic1.get(t[i],0)-1
        for j in dic1:
            if dic1[j]>0:
                return False
        return True