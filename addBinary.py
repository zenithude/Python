# -*- coding: utf-8 -*-
"""
@author : zenithude

Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"



Constraints:

    Each string consists only of '0' or '1' characters.
    1 <= a.length, b.length <= 10^4
    Each string is either "0" or doesn't contain any leading zero.


"""


class Solution:
    def addBinary(self, a, b):
        """

        :param a : str
        :param b : str
        :return : str
        """
        n1 = int(a, 2)
        n2 = int(b, 2)
        n3 = n1 + n2
        temp = str(bin(n3))
        result = temp[2:]

        return result


obj = Solution()
a = "1010"
b = "1011"
print(obj.addBinary(a, b))