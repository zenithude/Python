# -*- coding: utf-8 -*-
"""
@author : zenithude

Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid
palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false



Constraints:

    s consists only of printable ASCII characters.


"""


class Solution1:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        list_s = []
        for caract in s:
            if caract.isalpha():
                list_s.append(caract.lower())
            if caract.isnumeric():
                list_s.append(caract)

        list_s1 = []

        for i in range(len(list_s) - 1, -1, -1):
            list_s1.append(list_s[i])

        return list_s1 == list_s


class Solution:
    def isPalindrome(self, s):
        beg, end = 0, len(s) - 1
        while beg <= end:
            while not s[beg].isalnum() and beg < end: beg += 1
            while not s[end].isalnum() and beg < end: end -= 1
            if s[beg] == s[end] or s[beg].upper() == s[end].upper():
                beg, end = beg + 1, end - 1
            else:
                return False
        return True


obj = Solution()
print(obj.isPalindrome("0P"))
