# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 13:29:37 2020

@author: zenit

 Subarray sum Equals K

Given an array of integers and an integer k, you need to find the total number 
of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the 
    integer k is [-1e7, 1e7].

   Hide Hint #1  
Will Brute force work here? Try to optimize it.

   Hide Hint #2  
Can we optimize it by using some extra space?

   Hide Hint #3  
What about storing sum frequencies in a hash table? Will it be useful?

   Hide Hint #4  
sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the 
elements from index i to j-1. Can we use this property to optimize it.


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
"""

from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        """
        Parameters
        ----------
        nums : List[int]
        
        k : int
            
        Returns
        -------
        int
        """         
        prevSum = defaultdict(lambda : 0)        
        res = 0
        n = len(nums)         
        currsum = 0 
        
        for i in range(0, n):          
            currsum += nums[i]
            if currsum == k:
                res += 1         
            if (currsum - k) in prevSum:
                res += prevSum[currsum - k]
                  
            prevSum[currsum] += 1           
        return res
    
s =Solution()
nums = [1,1,1]
k = 2
print(s.subarraySum(nums, k))