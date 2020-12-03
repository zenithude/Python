# -*- coding: utf-8 -*-
"""
@author : zenithude

Reverse Words in a String

Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: "  hello world!  "
Output: "world! hello"

Explanation: Your reversed string should not contain leading or trailing
spaces.

Example 3:

Input: "a good   example"
Output: "example good a"

Explanation: You need to reduce multiple spaces between two words to a
single space in the reversed string.

Note:

    A word is defined as a sequence of non-space characters.

    Input string may contain leading or trailing spaces. However,
    your reversed string should not contain leading or trailing spaces.

    You need to reduce multiple spaces between two words to a single space
    in the reversed string.

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
"""


class Solution:
    def reverseWords(self, s):
        """

        :param s: str
        :return: str
        """
        if not s:
            return
        list_word = s.split(" ")
        list_word.reverse()
        i = 0
        if "" in list_word:
            while i < len(list_word):
                if list_word[i] == "":
                    del list_word[i]
                    i -= 1
                i += 1
        result = " ".join(list_word)
        return result


obj = Solution()
s = "gddfg   fgd gfgdfg gfefef"
print(obj.reverseWords(s))