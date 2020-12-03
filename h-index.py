# -*- coding: utf-8 -*-
"""
@author : zenithude

Given an array of citations (each citation is a non-negative integer) of a
researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index
h if h of his/her N papers have at least h citations each, and the other N −
h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3

Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
of them had received 3, 0, 6, 1, 5 citations respectively.

Since the researcher has 3 papers with at least 3 citations each and the
remaining two with no more than 3 citations each, her h-index is 3.

Note: If there are several possible values for h, the maximum one is taken
as the h-index.

"""
from bisect import bisect_right


class Solution_1:
    def hIndex(self, citations):
        """

        :param citations : List[int]
        :return: int
        """
        citations.sort(reverse=True)
        ans = 0
        for i, c in enumerate(citations, 1):
            if c >= i: ans = i
        return ans


class Solution_2:
    def hIndex(self, citations):
        """

        :param citations : List[int]
        :return: int
        """
        return next(
                (len(citations) - i for i, x in enumerate(sorted(citations)) if
                 len(citations) - i <= x), 0)


class Solution:
    def hIndex(self, citations):
        """

        :param citations : List[int]
        :return: int
        """
        return bisect_right([i - c for i, c in
                             enumerate(sorted(citations, reverse=True), 1)], 0)


citations = [3, 0, 6, 1, 5]
obj_1 = Solution_1()
obj_2 = Solution_2()
obj = Solution()
print(obj_1.hIndex(citations))
print(obj_2.hIndex(citations))
print(obj.hIndex(citations))
