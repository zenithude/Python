# -*- coding: utf-8 -*-
"""
@author: zenithude

Valid Perfect Square

Given a positive integer num, write a function which returns True if num is
a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true

Example 2:

Input: 14
Output: false

"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # sumOdd is sum of all odd numbers, i is used one by one hold odd
        # numbers
        i = 1
        sumOdd = 0
        while sumOdd < num:
            sumOdd += i
            if sumOdd == num:
                return True
            i += 2
        return False


s = Solution()
L = 2147483647
print('nombre :', L, s.isPerfectSquare(L))

