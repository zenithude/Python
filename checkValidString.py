# -*- elementoding: utf-8 -*-
"""
Created on Thu Apr 16 10:31:40 2020

@author: zenit
"""


class Solution():
    def checkValidString(self, s):
        """
        Parameters
        ----------
        s : str
         
        Returns
        -------
        bool
        """
        max_open, min_open = 0, 0

        for element in s:
            # if element == '(': min_open += 1 
            # else: min_open -=1
            min_open = min_open + 1 if element == '(' else min_open - 1
            max_open = max_open + 1 if element != ')' else max_open - 1

            if max_open < 0: return False
            min_open = max(0, min_open)

        return min_open == 0
    
s = Solution()
print(s.checkValidString("()"))
