# -*- coding: utf-8 -*-
"""
@author : zenithude

Single Number III

Given an array of numbers nums, in which exactly two elements appear only
once and all the other elements appear exactly twice. Find the two elements
that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]

Note:

    The order of the result is not important. So in the above example, [5,
    3] is also correct.

    Your algorithm should run in linear runtime complexity. Could you
    implement it using only constant space complexity?

"""


class Solution:
    def singleNumber(self, nums):
        """

        :param nums : List[int]
        :return : List[int]
        """
        if not nums:
            return [0, 0]
        count = 0
        result = []
        deja_vu = []
        for element in nums:
            if nums.count(element) == 1 and element not in deja_vu:
                result.append(element)
                count += 1
            else:
                deja_vu.append(element)
            if count == 2:
                return result


obj = Solution()
nums = [1, 2, 1, 2, 1, 4, 6, 2, 6, 4, 1, 3, 2, 5]
print(obj.singleNumber(nums))
