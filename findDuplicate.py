# -*- coding: utf-8 -*-
"""
@author : zenithude

"""


class Solution:
    def findDuplicates(self, nums):
        """

        :param nums : List[int]
        :return : List[int]
        """
        for i in range(len(nums)):
            while i != nums[i] - 1 and nums[i] != nums[nums[i] - 1]:
                temp = nums[i] - 1
                nums[i], nums[temp] = nums[temp], nums[i]

        return [nums[it] for it in range(len(nums)) if it != nums[it] - 1]


obj = Solution()
arr = [1, 2, 3, 1, 3, 6, 6]
print(obj.findDuplicates(arr))