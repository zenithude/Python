# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:29:50 2020

@author: zenit Given a non-empty array of integers, every element appears
twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it
 without using extra memory?
"""


class Solution:
    def singleNumber(self, nums):
        """
        Parameters
        ----------
        nums : list[int]
           
        Returns
        -------
        int            
        """
        dejavu = []
        for element in nums:
            if element not in dejavu:
                dejavu.append(element)
            else:
                dejavu.remove(element)
        return dejavu.pop()