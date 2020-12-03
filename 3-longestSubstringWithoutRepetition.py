# -*- coding: utf-8 -*-
"""
@author : zenithude

Given a string, find the length of the longest substring without repeating
characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

             Note that the answer must be a substring, "pwke" is a
             subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """

        :param s : str
        :return  : int
        """
        longest, cur_len, start, d = 0, 0, 0, set()
        for i in range(len(s)):
            cur_len += 1
            while s[i] in d:
                d.remove(s[start])
                cur_len -= 1
                start += 1
            longest = max(cur_len, longest)
            d.add((s[i]))
        return longest


obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))
print(obj.lengthOfLongestSubstring("bbbbb"))
print(obj.lengthOfLongestSubstring("pwwkew"))