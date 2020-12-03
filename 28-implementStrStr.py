# -*- coding: utf-8 -*-
"""
@author : zenithude

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

"""


class Solution:
    def strStr(self, haystack, needle):
        """
        Return the index of first occurence of needle in haystack.

        :param haystack : str
        :param needle : str
        :return : int
        """
        if needle not in haystack:
            return -1
        elif not needle:
            return 0
        else:
            return haystack.index(needle)


obj = Solution()
haystack = ""
needle = ""
print(obj.strStr(haystack, needle))
