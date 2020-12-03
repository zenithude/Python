# -*- coding: utf-8 -*-
"""
@author : zenithude

Given an array nums of n integers, are there elements a, b, c in nums such
that a + b + c = 0? Find all unique triplets in the array which gives the
sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution1:
    def threeSum(self, nums):
        """
        Return all unique triplets with Sum = 0

        :param nums: : List[int]
        :return: List[List[int]]
        """
        if not nums:
            return None
        triplets = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sum3 = [nums[i], nums[j], nums[k]]
                        if sum3 not in triplets:
                            triplets.append(sum3)
        return triplets


class Solution2:
    def threeSum(self, nums):
        """
        Return all unique triplets with Sum = 0

        :param nums: : List[int]
        :return: List[List[int]]
        """
        if not nums:
            return None
        triplets = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    sum3 = [nums[i], nums[j], nums[k]]
                    if sum3 not in triplets:
                        triplets.append(sum3)
                    # while j < n - 1 and nums[j] == nums[j + 1]: j += 1
                    # while k > 0 and nums[k] == nums[k - 1]: k -= 1
                    j += 1
                    k -= 1
        return triplets


class Solution3:
    def threeSum(self, nums):
        """
        Return all unique triplets with Sum = 0

        :param nums: : List[int]
        :return: List[List[int]]
        """
        if not nums:
            return None
        triplets = []
        nums = sorted(nums)
        n = len(nums)

        for i in range(n):
            target = -nums[i]
            j, k = i + 1, n - 1
            while j < k:
                sum2 = nums[j] + nums[k]
                if sum2 < target:
                    j += 1
                elif sum2 > target:
                    k -= 1
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in triplets:
                        triplets.append(triplet)
                        j += 1
                        k -= 1
        return triplets


class Solution:
    def threeSum(self, nums):
        """
        Return all unique triplets with Sum = 0

        :param nums: : List[int]
        :return: List[List[int]]
        """
        if not nums:
            return None
        triplets = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue
            if 0 < i and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    while j < k - 1 and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                elif tmp < 0:
                    j += 1
                else:
                    k -= 1
        return triplets


obj = Solution()
nums = [-1, 0, 1, 2, -1, -4]
nums1 = [-2, 0, 1, 1, 2]
print(obj.threeSum(nums1))
