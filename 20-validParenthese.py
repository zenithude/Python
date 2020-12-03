# -*- coding: utf-8 -*-
"""
@author : zenithude

Given a string containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        if len(s) % 2 != 0:
            return False
        stack, table = [], {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in {'(', '[', '{'}:
                stack.append(char)
            elif not stack or table[char] != stack[-1]:
                return False
            else:
                stack.pop()
        return not stack


obj = Solution()
strs = "(([]){})"
strs1 = "[([]])"

print(obj.isValid(strs))

