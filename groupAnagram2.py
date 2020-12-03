# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 01:24:17 2020

@author: zenit
Given an array of strings, group anagrams together.
"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        """
        Parameters
        ----------
        strs : List[str]
            

        Returns
        -------
        List[List[str]]
        """
        anagram = defaultdict(list)
        strsFinal = []
        for element in strs:
            anagram["".join(sorted(element))].append(element)

        for element in anagram.values():
            strsFinal.append(element)
        
        return strsFinal
                    
        
s = Solution()
test = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(test))
        