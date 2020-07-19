# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 19:27:12 2020

@author: MyPC
"""

import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=collections.defaultdict(list)
        for s in strs:
            counter=[0]*26
            for c in s:
                counter[ord(c)-ord('a')]+=1
            result[tuple(counter)].append(s)
        return list(result.values())