# -*- coding: utf-8 -*-
"""
@author : zenithude

 Given a string, find the first non-repeating character in it and return
 it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.

"""
import collections


class Solution:
    def firstUniqChar(self, s):
        """
        function which returns the index of the 1st single character of a
        string given
        :param s: str
        :return: int

        """
        counter = collections.Counter(s)
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
        return -1


s = Solution()
print(s.firstUniqChar('loveleetcode'))