# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:55:09 2020

@author: zenit

Given an array nums of n integers where n > 1,  return an array output such 
that output[i] is equal to the product of all the elements of nums except 
nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or
 suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does 
not count as extra space for the purpose of space complexity analysis.)

"""

class Solution:
    def productExceptSelf(self, nums):
        """
        Parameters
        ----------
        nums : list(int)

        Returns
        -------
        list(int)
        """
        right_multiply = [0] * len(nums)
        right_multiply[-1]=nums[-1]
        for i in range(1,len(nums)):
            right_multiply[len(nums)-i-1] = right_multiply[len(nums)- i] * nums[len(nums)-i-1]
        output = [0]*len(nums)
        prefix = 1
        current_index = 0
        while current_index < len(output)-1:
            output[current_index] = prefix * right_multiply[current_index+1]
            prefix *= nums[current_index]
            current_index +=1
        output[-1] = prefix
        return output

s = Solution()
print(s.productExceptSelf([1,2,3,4]))
