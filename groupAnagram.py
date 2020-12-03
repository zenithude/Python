# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 01:24:17 2020

@author: zenit
Given an array of strings, group anagrams together.
"""

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
        i = 0
        strsFinal=[]
        while i < len(strs):
            strs1 = []
            j = 0
            while j < len(strs):
                if sorted(strs[i]) == sorted(strs[j]):
                    strs1.append(strs[j])
                j += 1
            i += 1
            if strs1 not in strsFinal:
                strsFinal.append(strs1)
                    
        return strsFinal
                    
        
s = Solution()
test = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(test))
        