# -*- coding: utf-8 -*-
"""
@author : zenithude

Write a function to find the longest common prefix string amongst an array
of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.

"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if len(strs) < 1:
            return prefix
        elif len(strs) == 1:
            return strs[0]
        for i in range(len(strs) - 1):
            prefix = self.commonPrefix(strs[i], strs[i + 1], prefix)
            if prefix == "":
                return prefix
        return prefix

    def commonPrefix(self, string1, string2, prefix):
        """

        :param string1: str
        :param string2: str
        :return: str
        """
        if prefix != "":
            if string1.startswith(prefix) and string2.startswith(prefix):
                return prefix

        prefix, longueur1, longueur2 = "", len(string1), len(string2)
        if longueur1 <= longueur2:
            longueur = longueur1
        else:
            longueur = longueur2
        for i in range(longueur):
            if string1[i] == string2[i]:
                prefix += string1[i]
            else:
                return prefix

        return prefix


s = Solution()
strs = ["acc","aaa","aaba"]
strs1 = ["flower", "flow", "flight"]
print(s.longestCommonPrefix(strs))
print(s.longestCommonPrefix(strs1))
