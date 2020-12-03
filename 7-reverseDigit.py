# -*- coding: utf-8 -*-
"""
@author : zenithude
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note: Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range: [−2**31,  2**31 − 1]. For the
purpose of this problem, assume that your function returns 0 when the
reversed integer overflows.


Remarque: Supposons que nous ayons affaire à un environnement qui ne
pourrait stocker que des entiers dans la plage d'entiers signés 32 bits: [
−2**31, 2**31 - 1]. Aux fins de ce problème, supposez que votre fonction
renvoie 0 lorsque l'entier inversé déborde.

"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -2 ** 31 < x < 2 ** 31 - 1:
            listX = list(str(abs(x)))
            listX.reverse()
            if x < 0:
                y = '-' + ''.join(listX)
            else:
                y = ''.join(listX)
            if -2 ** 31 < int(y) < 2 ** 31 - 1:
                return int(y)
            else:
                return 0
        return 0


s = Solution()
print(s.reverse(-130))

x = 5321252021
print(s.reverse(x))
print(x < 2 ** 31)
