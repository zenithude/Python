# -*- coding: utf-8 -*-
"""
@author : zenithude

 Numbers With Same Consecutive Differences

Return all non-negative integers of length N such that the absolute
difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for
the number 0 itself. For example, 01 has one leading zero and is invalid,
but 0 is valid.

You may return the answer in any order.

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]

Explanation: Note that 070 is not a valid number, because it has leading
zeroes.

Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Note:

    1 <= N <= 9
    0 <= K <= 9


"""
from functools import reduce


class Solution:
    def numsSameConsecDiff(self, N, K):
        """

        :param N: int
        :param K: int
        :return: List[int]
        """
        res = []

        def dfs(cur):
            if len(cur) == N:
                if cur[0] == 0 and len(cur) > 1: return
                res.append(reduce(lambda x, y: x * 10 + y, cur))
                return
            if K != 0:
                if cur[-1] + K < 10:
                    dfs(cur + [cur[-1] + K])
                if cur[-1] - K >= 0:
                    dfs(cur + [cur[-1] - K])
            else:
                dfs(cur + [cur[-1] + K])

        for i in range(10):
            dfs([i])
        return res


obj = Solution()
print(obj.numsSameConsecDiff(2, 1))