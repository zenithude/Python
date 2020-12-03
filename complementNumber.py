# -*- coding: utf-8 -*-
"""
@author : zenithude

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary
representation.



Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to
output 2.



Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to
output 0.



Note:

    The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    You could assume no leading zero bit in the integer’s binary representation.
    This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

"""


class Solution:
    def findComplement(self, num: int) -> int:
        """
        :param num: int
        :return: int
        """
        chaine = bin(num)
        result = self.flip(chaine)
        return int(result, 2)

    def flip(self, chaine: str) -> str:
        """
        :param chaine: str
        :return: str
        """
        chaine1, result = '', '0b'
        for i in range(2, len(chaine)):
            if chaine[i] == '0':
                chaine1 += '1'
            else:
                chaine1 += '0'
        return result + chaine1


s = Solution()
print(s.findComplement(10))
