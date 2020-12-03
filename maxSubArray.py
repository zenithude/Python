# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:31:25 2020

@author: zenit

Given an integer array nums, find the contiguous subarray (containing at least 
one number) which has the largest sum and return its sum.
"""

class Solution:
   def maxSubArray(self, nums):
       intermediaireMax = 0
       finMax = nums[0]
       for i in range(0, len(nums)):
           intermediaireMax += nums[i]
           if finMax < intermediaireMax:
               finMax = intermediaireMax
           if intermediaireMax < 0:
               intermediaireMax = 0
       return finMax

s = Solution()
print(s.maxSubArray([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]))



