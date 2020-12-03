# -*- coding: utf-8 -*-
"""
@author : zenithude

You are given an array coordinates, coordinates[i] = [x, y], where [x,
y] represents the coordinate of a point. Check if these points make a
straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false



Constraints:

    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.
"""


class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) == 2:
            return True
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
                return False
        return True


test = [[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]]
test_1 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
test_2 = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
test_3 = [[0, 1], [1, 3], [-4, -7], [5, 11]]
s = Solution()
print(s.checkStraightLine(test))
print(s.checkStraightLine(test_1))
print(s.checkStraightLine(test_2))
print(s.checkStraightLine(test_3))

