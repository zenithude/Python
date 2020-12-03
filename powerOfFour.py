# -*- coding: utf-8 -*-
"""
@author : zenithude
Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a
power of 4.

Example 1:

Input: 16
Output: true

Example 2:

Input: 5
Output: false

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfFour(self, num):
        """

        :param num : int
        :return : bool
        """

        return (num != 0 and ((num & (num - 1)) == 0) and not (
                    num & 0xAAAAAAAA))


obj = Solution()
print(obj.isPowerOfFour(-16))
print(obj.isPowerOfFour(-2147483648))
print(obj.isPowerOfFour(0))
print(obj.isPowerOfFour(8**4))
print(obj.isPowerOfFour(16))
print(obj.isPowerOfFour(4))
