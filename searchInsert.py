#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: zenithude

Search Insert Position

Given a sorted array and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in
order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0


"""


class Solution:
    def searchInsert(self, nums, target):
        """

        :param nums: : List[int]
        :param target: int
        :return: int
        """
        if not nums:
            return 0
        if target in nums:
            return nums.index(target)
        elif target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        else:
            for i in range(1, len(nums)):
                if nums[i - 1] < target < nums[i]:
                    return i


nums = [1,3,5,6]
target = 2
obj = Solution()
print(obj.searchInsert(nums, target))
