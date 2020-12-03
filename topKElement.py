# -*- coding: utf-8 -*-
"""
@author : zenithude

Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.

    Your algorithm's time complexity must be better than O(n log n), where n
    is the array's size.

    It's guaranteed that the answer is unique, in other words the set of the
    top k frequent elements is unique.

    You can return the answer in any order.

"""


class Solution1:
    def topKFrequent(self, nums, k):
        """
        Solution exceed time limit
        :param nums : List[int]
        :param k: int
        :return : List[int]
        """
        result = []
        dict_nums = {}
        for num in nums:
            if num not in dict_nums.keys():
                dict_nums[num] = nums.count(num)
        while k > 0:
            for key, value in dict_nums.items():
                if value == max(dict_nums.values()):
                    result.append(key)
                    dict_nums.pop(key)
                    break
            k -= 1
        return result


class Solution:
    def topKFrequent(self, nums, k):
        """

        :param nums : List[int]
        :param k: int
        :return : List[int]
        """
        number_frequency = {}
        frequency_list = {}
        for i in nums:
            if i not in number_frequency:
                number_frequency[i] = 1
            else:
                number_frequency[i] += 1
        for key, value in number_frequency.items():
            if value not in frequency_list:
                frequency_list[value] = [key]
            else:
                frequency_list[value].append(key)
        result = []
        for i in range(len(nums), 0, -1):
            if i in frequency_list:
                result.extend(frequency_list[i])
            if len(result) >= k:
                break
        return result


obj = Solution()
nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
k = 2
print(obj.topKFrequent(nums, k))