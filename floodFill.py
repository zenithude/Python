# -*- coding: utf-8 -*-
"""@author : zenithude

An image is represented by a 2-D array of integers,
each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column)
of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (
also with the same color as the starting pixel), and so on. Replace the
color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]] sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image
(with position (sr, sc) = (1, 1)), all pixels connected by a path of the
same color as the starting pixel are colored with the new color. Note the
bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note: The length of image and image[0] will be in the range [1, 50]. The
given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc <
image[0].length. The value of each color in image[i][j] and newColor will be
an integer in [0, 65535].

"""


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        M, N = len(image), len(image[0])
        prevC = image[sr][sc]
        self.floodFillUtil(image, sr, sc, prevC, newColor)

        return image

    # A recursive function to replace
    # previous color 'prevC' at '(x, y)'
    # and all surrounding pixels of (x, y)
    # with new color 'newC' and
    def floodFillUtil(self, screen, x, y, prevC, newC):
        # Base cases
        M, N = len(screen), len(screen[0])
        if (x < 0 or x >= M or y < 0 or y >= N or screen[x][y] != prevC or
                screen[x][y] == newC):
            return

        # Replace the color at (x, y)
        screen[x][y] = newC

        # Recur for north, east, south and west
        self.floodFillUtil(screen, x + 1, y, prevC, newC)
        self.floodFillUtil(screen, x - 1, y, prevC, newC)
        self.floodFillUtil(screen, x, y + 1, prevC, newC)
        self.floodFillUtil(screen, x, y - 1, prevC, newC)


# Driver Code
screen = [[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1], [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0], [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1], [1, 1, 1, 1, 1, 2, 2, 1]]
M, N = len(screen), len(screen[0])
x = 4
y = 4
newC = 3
s = Solution()
s.floodFill(screen, x, y, newC)

print("Updated screen after call to floodFill:")
for i in range(M):
    for j in range(N):
        print(screen[i][j], end=' ')
    print()