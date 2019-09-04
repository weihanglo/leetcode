#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question: https://leetcode.com/problems/house-robber/
#
# You are a professional robber planning to rob houses along a street. Each 
# house has a certain amount of money stashed, the only constraint stopping 
# you from robbing each of them is that adjacent houses have security system 
# connected and it will automatically contact the police if two adjacent houses 
# were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight
# without alerting the police.

# Recursive. **TLE** solution.
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        def rob_helper(k, nums):
            # Base cases
            if k == 0: # f(0)
                return nums[k]
            if k == 1: # f(1)
                return max(nums[k], nums[k - 1])
            # f(k)
            return max(
                rob_helper(k - 2, nums) + nums[k], 
                rob_helper(k - 1, nums)
            )
        return rob_helper(len(nums) - 1, nums)

# Iterative.
# https://leetcode.com/problems/house-robber/discuss/55696
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev =  current = 0
        for num in nums:
            prev, current = current, max(prev + num, current)
        return current
