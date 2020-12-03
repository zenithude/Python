# -*- coding: utf-8 -*-
"""
@author : zenithude

 Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1
represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid
is completely surrounded by water, and there is exactly one island (i.e.,
one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the
water around the island). One cell is a square with side length 1. The grid
is rectangular, width and height don't exceed 100. Determine the perimeter
of the island.

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
"""


# Find the number of covered side for mat[i][j].
def numofneighbour(mat, i, j):
    count = 0
    R = len(mat)
    C = len(mat[0])

    # UP
    if i > 0 and mat[i - 1][j]:
        count += 1

    # LEFT
    if j > 0 and mat[i][j - 1]:
        count += 1

    # DOWN
    if i < R - 1 and mat[i + 1][j]:
        count += 1

    # RIGHT
    if j < C - 1 and mat[i][j + 1]:
        count += 1

    return count


class Solution:
    def islandPerimeter(self, grid):
        """
        Return perimeter of island in grid.

        :param grid: : List[List[int]]
        :return: int
        """
        if not grid:
            return 0
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    perimeter += (4 - numofneighbour(grid, i, j))
        return perimeter


island = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

obj = Solution()
print(obj.islandPerimeter(island))
