# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:45:18 2020

@author: zenit
Given two strings S and T, return if they are equal when both are typed into 
empty text editors. # means a backspace character
"""
def newString(S):  
      
        q = []  
      
        for i in range(0, len(S)):  
      
            if S[i] != '#':  
                q.append(S[i])  
            elif len(q) != 0:  
                q.pop()  
      
        # Build final string  
        newS = ""  
      
        while len(q) != 0:  
            newS += q[0]  
            q.pop(0)  
      
        # return final string  
        return newS

class Solution:
    
    def backSpaceCompare(self, s: str, t: str) -> bool:
        """
        Parameters
        ----------
        s : str
            string only lowercase and # characters
        t : str
            string only lowercase and # characters

        Returns
        -------
        bool
            True if s and t are equals

        """
        s1 = newString(s)
        s2 = newString(t)
        if s1 == s2:
            return True
        else:
            return False
        
s = Solution()
s1 = 'ab#c'
s2 = 'ad#c'
print(s.backSpaceCompare(s1, s2))
