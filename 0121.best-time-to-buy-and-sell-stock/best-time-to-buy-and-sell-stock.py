#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# Say you have an array for which the ith element is the price of a given stock 
# on day i.
#
# If you were only permitted to complete at most one transaction 
# (ie, buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.
# 
# Example 1:
# 
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# 
# max. difference = 6-1 = 5 
# (not 7-1 = 6, as selling price needs to be larger than buying price)
# 
# Example 2:
# 
# Input: [7, 6, 4, 3, 1]
# Output: 0
# 
# In this case, no transaction is done, i.e. max profit = 0.

import sys
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = sys.maxsize
        profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > profit:
                profit = p - min_price
        return profit
