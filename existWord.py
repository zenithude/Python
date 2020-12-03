# -*- coding: utf-8 -*-
"""
@author : zenithude

Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring. The
same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.



Constraints:

    board and word consists only of lowercase and uppercase English letters.
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3


"""


class Solution(object):
    def exist(self, board, word):
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if word[0] == board[i][j]:
                    if self.find(board, word, i, j):
                        return True
        return False

    def find(self, board, word, row, col, i=0):
        if i == len(word):
            return True
        if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0 or \
                word[i] != board[row][col]:
            return False
        board[row][col] = '*'
        res = (self.find(board, word, row + 1, col, i + 1)
               or self.find(board, word, row - 1,  col, i + 1)
               or self.find(board, word, row, col + 1, i + 1)
               or self.find(board, word, row, col - 1, i + 1))
        board[row][col] = word[i]
        return res


obj = Solution()
board = [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']]

word = "ABCCED"
word1 = "SEE"
word2 = "ABCB"
print(obj.exist(board, word))
print(obj.exist(board, word1))
print(obj.exist(board, word2))