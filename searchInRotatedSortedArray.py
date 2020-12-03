# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:00:16 2020

@author: zenit

Suppose an array sorted in ascending order is rotated at some pivot unknown 
to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index,
 otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


"""

class Solution:
    def search(self, nums, target):
        """
        Parameters
        ----------
        nums : List[List(int)]
        target : int
        
        Returns
        -------
        int
        """
        if target in nums:
            return nums.index(target)
        else:
            return -1
        
s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
