# -*- coding: utf-8 -*-
"""
@author : zenithude

Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word (last word means the last
appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space
characters only.

Example:

Input: "Hello World"
Output: 5

"""


class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or s == ' ':
            return 0
        if ' ' not in s:
            return len(s)

        list_word = s.split(' ')
        print(list_word)
        while "" in list_word:
            list_word.remove("")
        if len(list_word) == 0:
            return 0
        return len(list_word[-1])


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start, end = -1, -1  # start and end of last word
        for j in range(len(s)):
            if s[j] != " ":
                end = j
                if j == 0 or s[j - 1] == " ":
                    start = j
        if start == -1:
            return 0
        return end - start + 1


s = ' a'
obj = Solution()
print(obj.lengthOfLastWord(s))