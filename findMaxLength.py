#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: zenithude

Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with
equal number of 0 and 1.

Example 1:

Input: [0,1] Output: 2 Explanation: [0, 1] is the longest contiguous
subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0] Output: 2 Explanation: [0, 1] (or [1, 0]) is a longest
contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.

"""


# Utility functions to find minimum
# and maximum of two elements
def min(x, y):
    return x if (x < y) else y


def max(x, y):
    return x if (x > y) else y


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        # Initialize result
        max_len = 1
        _len = 1
        for i in range(n - 1):
            if nums[i] == 0 and nums[i + 1] in [1,2,3,4,5,6,7,8,9]:
                _len += 1
            elif nums[i] in [1,2,3,4,5,6,7,8,9] and nums[i + 1] == 0:
                _len += 1
            else:
                _len = 1
            if _len > max_len:
                max_len += _len
        if max_len % 2 == 0:
            return max_len
        else:
            return max_len - 1


obj = Solution()
print(obj.findMaxLength([0,1,0,2,2,0,0,1]))