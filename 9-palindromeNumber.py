# -*- coding: utf-8 -*-
"""
@author : zenithude

Determine whether an integer is a palindrome. An integer is a palindrome
when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121 Output: false Explanation: From left to right, it reads -121.
From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""


class Solution(object):
    def isPalindrome(self, x):
        """
        Simple avec transformation en string
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        y = list(str(x))
        z = list(str(x))
        z.reverse()
        return y == z

    def isPalindrome2(self, x):
        """
        Sans transformation en string
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        nx = x
        r = 0
        while nx > 0:
            u = nx % 10
            r = r * 10 + u
            nx = nx // 10
        return x == r


s = Solution()
print(s.isPalindrome2(225))
print(s.isPalindrome2(121))
print(s.isPalindrome2(-121))
print(s.isPalindrome2(10))