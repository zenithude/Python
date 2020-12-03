# -*- coding: utf-8 -*-
"""
@author : zenithude

Given a string which consists of lowercase or uppercase letters, find the
length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

"""
from collections import Counter


class Solution:
    def longestPalindrome(self, s):
        """

        :param s : str
        :return : int
        """
        odds = sum([freq % 2 for _, freq in Counter(s).items()])
        return len(s) if odds <= 1 else len(s) - odds + 1


obj = Solution()
print(obj.longestPalindrome("abccccdd"))
