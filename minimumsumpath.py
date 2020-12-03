# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:29:37 2020

@author: zenit

Given a m x n grid filled with non-negative numbers, find a path from top left 
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


"""

class Solution:
    def minPathSum(self, grid):
        """
        Parameters
        ----------
        grid : List[List(int)]
   
        Returns
        -------
        int
        """
        row = len(grid) - 1
        column = len(grid[0]) - 1
        i = row - 1
        j = column - 1
        while j >= 0:
            grid[row][j] += grid[row][j+1]
            j -= 1
        while i >= 0:
            grid[i][column] += grid[i+1][column]
            i -= 1
        j = column - 1
        i = row - 1
        while i >= 0:
            while j >= 0:
                grid[i][j] += min(grid[i][j+1],grid[i+1][j])
                j -= 1
            j = column - 1
            i -= 1
        return (grid[0][0])

s = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(s.minPathSum(grid))