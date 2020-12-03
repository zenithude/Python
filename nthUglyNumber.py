# -*- coding: utf-8 -*-
"""
@author : zenithude
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12

Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
ugly numbers.

Note:

    1 is typically treated as an ugly number.
    n does not exceed 1690.

"""


class Solution:
    def nthUglyNumber(self, n):
        """
        Return the n-th ugly number
        :param n: int
        :return: int
        """
        if n < 1 or n > 1690:
            return None
        uglyNum = []
        i2, i3, i5 = 0, 0, 0
        next2mul, next3mul, next5mul = 2, 3, 5
        nextUgly = 1
        uglyNum.append(nextUgly)
        for i in range(1, n):
            nextUgly = min(next2mul, next3mul, next5mul)
            uglyNum.append(nextUgly)

            if nextUgly == next2mul:
                i2 += 1
                next2mul = uglyNum[i2] * 2
            if nextUgly == next3mul:
                i3 += 1
                next3mul = uglyNum[i3] * 3
            if nextUgly == next5mul:
                i5 += 1
                next5mul = uglyNum[i5] * 5

        return nextUgly


obj = Solution()
print(obj.nthUglyNumber(1690))