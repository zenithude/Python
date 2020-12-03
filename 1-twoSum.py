# -*- coding: utf-8 -*-
"""
@author : zenithude

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        maps = {}
        for i, n in enumerate(nums):
            left = target - n
            if left in maps:
                return [maps[left], i]

            maps[n] = i


nums = [2, 7, 11, 15, 65, 4, 32, 9, 25, 62, 102, 8]
s = Solution()
target = 9
print(s.twoSum(nums, target))