#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zenprog

Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how many square submatrices have
 all ones.


Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1
There is 1 square of side 2
Total number of squares = 6 + 1 = 7.


Constraints:

    1 <= arr.length <= 300
    1 <= arr[0].length <= 300
    0 <= arr[i][j] <= 1


"""


class Solution(object):
    """Object to test."""

    def countSquares(self, matrix):
        """
        Return how many square submatrices have all ones.

        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        result = 0
        n, m = len(matrix), len(matrix[0])
        for i in range(0, m):
            result += matrix[n - 1][i]
        for i in range(0, n):
            result += matrix[i][m - 1]
        result -= matrix[n - 1][m - 1]
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                if matrix[i][j] == 1:
                    matrix[i][j] = 1 + min(matrix[i + 1][j + 1],
                                           matrix[i][j + 1], matrix[i + 1][j])
                else:
                    matrix[i][j] = 0
                result += matrix[i][j]
        return result


obj = Solution()
matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
matrix1 = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
print(obj.countSquares(matrix))
print(obj.countSquares(matrix1))
