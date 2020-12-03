# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:24:27 2020

@author: zenit
"""
class Solution:
    
    def min(self, x, y): 
        return x if(x < y) else y 
      
    def max(self, x, y): 
        return x if(x > y) else y 
  
    # Returns length of the longest 
    # contiguous subarray 
    def findMaxLength(self, arr): 
        n = len(arr)
        # Initialize result 
        max_len = 1 
        for i in range(n - 1): 
          
            # Initialize min and max for 
            # all subarrays starting with i 
            mn = arr[i] 
            mx = arr[i] 
      
            # Consider all subarrays starting 
            # with i and ending with j 
            for j in range(i + 1, n): 
              
                # Update min and max in 
                # this subarray if needed 
                mn = min(mn, arr[j]) 
                mx = max(mx, arr[j]) 
      
                # If current subarray has 
                # all contiguous elements 
                if ((mx - mn) == j - i): 
                    max_len = max(max_len, mx - mn + 1) 
              
        return max_len  

s = Solution()
print(s.findMaxLength([0,1,0,1]))