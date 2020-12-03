# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:48:42 2020

@author: zenit

Say you have an array for which the ith element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (i.e., buy one and sell one share of the stock
multiple times).

Note: You may not engage in multiple transactions at the same time (i.e.,
you must sell the stock before you buy again). """


class Solution:
    def maxProfit(self, prices):
        """
        Parameters
        ----------
        prices : List[int]

        Returns
        -------
        int
        """
        profit = 0
        i = 0 
        while i < (len(prices) - 1):
            while (i < (len(prices) - 1)) and (prices[i + 1] <= prices[i]):
                i += 1
            if i == (len(prices) - 1):
                break
            
            achete = i
            i += 1
            
            while (i < len(prices)) and prices[i] >= prices[i - 1]:
                i += 1
            
            vendre = i - 1
            
            profit += prices[vendre] - prices[achete]
        return profit

s = Solution()
l = [1,2,3,0,2]
print(s.maxProfit(l))
