# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 00:03:52 2020

@author: zenit
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.
"""


class Solution:
    def countElements(self, arr):
        """
        Parameters
        ----------
        arr : List(int)

        Returns
        -------
        int
        """
        count = 0
        for element in arr:
            if (element + 1) in arr:
                count += 1
                
        return count        
