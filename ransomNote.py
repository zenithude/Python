# -*- coding: utf-8 -*-
"""
@author : zenithude

(Given an arbitrary ransom note string and another string containing letters
from all the magazines, write a function that will return true if the ransom
note can be constructed from the magazines ; otherwise, it will return false.)

Each letter in the magazine string can only be used once in your ransom note. 

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "aab") -> true
canConstruct("aa", "ab") -> false
"""


class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :param ransomNote: str
        :param magazine: str
        :return: bool
        """
        if len(ransomNote) > len(magazine):
            return False

        dict_mag = {}
        for element in magazine:
            if element in dict_mag:
                dict_mag[element] += 1
            else:
                dict_mag[element] = 1

        for element in ransomNote:
            if element not in dict_mag:
                return False
            if dict_mag[element] <= 0:
                return False
            dict_mag[element] -= 1

        return True


R = "fffbfg"
S = "effjfggbffjdgbjjhhdegh"
note = Solution()
print(note.canConstruct(R, S))
