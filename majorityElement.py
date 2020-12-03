# -*- coding: utf-8 -*-
"""
@author: zenithude

Given an array of size n, find the majority element. The majority element is
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

"""
import time


class Solution:
    def majorityElement(self, nums):
        """
        :param nums: List(int)
        :return: int
        """
        global result
        counter = len(nums) // 2
        seen = []
        for num in nums:
            if num not in seen:
                seen.append(num)
                if nums.count(num) > counter:
                    counter = nums.count(num)
                    result = num

        return result


# Debut du decompte du temps
start_time = time.time()

s = Solution()
a = [2, 2, 1, 1, 1, 2, 2]
print(s.majorityElement(a))
final_time = round(time.time() - start_time, 5)

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % final_time)
