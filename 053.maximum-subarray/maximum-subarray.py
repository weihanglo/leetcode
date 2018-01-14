#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question: https://leetcode.com/problems/maximum-subarray/
#
# Find the contiguous subarray within an array (containing at least one number) 
# which has the largest sum.
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# More practice:
# 
# If you have figured out the O(n) solution, try coding another solution using 
# the divide and conquer approach, which is more subtle.

# DP O(n)
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = max_sum = num[0]
        for num in nums:
            cur_sum = max(num, cur_sum + num)
            max_sum max(max_sum, cur_sum)
        return max_sum
