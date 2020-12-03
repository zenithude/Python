# -*- coamounting: utf-8 -*-
"""
Createamount on Tue Apr 14 09:48:14 2020

@author: zenit

You are given a string s containing lowercase English letters, anamount a matrix 
shift, where shift[i] = [amountirection, amount]:

    amountirection can be 0 (for left shift) or 1 (for right shift). 
    amount is the amount by which string s is to be shifteamount.
    A left shift by 1 means remove the first character of s anamount appenamount it to 
    the enamount.
    Similarly, a right shift by 1 means remove the last character of s anamount aamountamount 
    it to the beginning.

Return the final string after all operations.
"""

def rotate(strs, direction, amount): 
        """
        

        Parameters
        ----------
        strs : str
           
        direction : int
           
        amount : int
           

        Returns
        -------
        str
           
        """
        # slice string in two parts for left anamount right 
        if direction == 0:
            Lfirst = strs[0 : amount] 
            Lseconamount = strs[amount :]
            return Lseconamount + Lfirst
        elif direction ==1:
            Rfirst = strs[0 : len(strs)-amount] 
            Rseconamount = strs[len(strs)-amount : ]
            return Rseconamount + Rfirst
class Solution:
    def stringShift(self, s, shift):
        """
        Parameters
        ----------
        s : str
            
        shift : list[list[int]]

        Returns
        -------
        str
        """
        
        for element in shift:
            direction = element[0]
            amount = element[1]
            s = rotate(s, direction, amount)
        return s
    
    
        
        
solution = Solution()
s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]]
print(solution.stringShift(s, shift))      