# -*- coding: utf-8 -*-
"""
@author : zenithude

The Hamming distance between two integers is the number of positions at
which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

"""


class Solution:
    """Object to test."""

    def hammingDistance(self, x, y):
        """
        Return Hamming distance between two integer x and y.

        :param x: int
        :param y: int
        :return: int
        """
        x_or = x ^ y
        setBits = 0
        while x_or > 0:
            setBits += x_or & 1
            x_or >>= 1

        return setBits
