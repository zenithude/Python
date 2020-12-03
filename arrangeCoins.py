# -*- coding: utf-8 -*-
"""
@author : zenithude.

You have a total of n coins that you want to form in a staircase shape,
where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed
integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

"""


class Solution1(object):
    """Object to Test."""
    def arrangeCoins(self, n):
        """
        Solution is low but ok.

        :param n: int
        :return: int
        """
        staircase = []
        k = 1
        while k <= n:
            staircase.append(k)
            n -= k
            k += 1
        return len(staircase)


def squareRoot(n):
    # We are using n itself as initial approximation
    # This can definitely be improved
    x = n
    y = 1

    e = 0.000001  # e decides the accuracy level
    while x - y > e:
        x = (x + y) / 2
        y = n / x

    return x


class Solution(object):
    """Object to Test."""
    def arrangeCoins(self, n):
        """
        Calculating portion inside the square root.

        :param n: int
        :return: int
        """
        N = 1 + 8 * n
        maxH = (-1 + squareRoot(N)) / 2
        return int(maxH)


obj = Solution()
print(obj.arrangeCoins(5))
print(obj.arrangeCoins(8))
print(obj.arrangeCoins(15))
