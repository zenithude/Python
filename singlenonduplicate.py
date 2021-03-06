﻿# -*- coding: utf-8 -*-
"""
@author : zenithude

Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element
appears exactly twice, except for one element which appears exactly once.
Find this single element that appears only once.



Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10

"""


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dejavu = []
        for element in nums:
            if element not in dejavu:
                dejavu.append(element)
            else:
                dejavu.remove(element)
        return dejavu.pop()