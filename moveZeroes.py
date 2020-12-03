# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:23:09 2020

@author: zenit

Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.
"""


class Solution1:
    def moveZeroes(self, nums):
        for element in nums:
            if element == 0:
                nums.remove(element)
                nums.append(element)


class Solution:
    def moveZeroes(self, nums):
        """

        :param nums: List[int]
        :return: nothins
        """
        if not nums:
            return

        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        return nums


l = [0, 1, 0, 3, 12]
s = Solution()
s.moveZeroes(l)
print(l)
