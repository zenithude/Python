# -*- coding: utf-8 -*-
"""
@author : zenithude
 Rotting Oranges

In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a
rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a
fresh orange.  If this is impossible, return -1 instead.



Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]] Output: -1 Explanation:  The orange in the
bottom left corner (row 2, column 0) is never rotten, because rotting only
happens 4-directionally.

Example 3:

Input: [[0,2]] Output: 0 Explanation:  Since there are already no fresh
oranges at minute 0, the answer is just 0.



Note:

    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    grid[i][j] is only 0, 1, or 2.


"""
from collections import deque


class Solution:
    def orangesRotting(self, grid):
        """

        :param grid : List[List[int]]
        :return : int
        """
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0

        result = 0
        sources = self.getsources(grid, m, n)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque(sources)
        level = 0
        while q:
            size = len(q)
            if level > 0:
                result += 1
            level += 1
            for k in range(size):
                i, j = q.popleft()

                for d in directions:
                    newi = i + d[0]
                    newj = j + d[1]
                    if m > newi >= 0 and n > newj >= 0 and grid[newi][
                        newj] == 1:
                        grid[newi][newj] = 2
                        q.append((newi, newj))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return result

    def getsources(self, grid, m, n):
        sources = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    sources.append((i, j))

        return sources
