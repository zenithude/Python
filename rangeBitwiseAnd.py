# -*- coding: utf-8 -*-
"""
Éditeur de Spyder


@author: zenit

Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND 
of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4

Example 2:

Input: [0,1]
Output: 0
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        Parameters
        ----------
        m : int
        n : int
        
        Returns
        -------
        int
        """
        steps = 0
        while m < n:
            m >>= 1
            n >>= 1
            steps += 1
            print('m = ', m, 'n = ', n, 'steps =', steps)
        print('m = ', m, 'steps =', steps, ' m << steps = ', (m << steps))   
        return m << steps

m = 5
n = 7
s = Solution()
print(s.rangeBitwiseAnd(m, n))