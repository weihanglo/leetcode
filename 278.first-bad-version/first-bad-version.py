#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/first-bad-version
#
# You are a product manager and currently leading a team to develop a new 
# product. Unfortunately, the latest version of your product fails the quality 
# check. Since each version is developed based on the previous version, 
# all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the 
# first bad one, which causes all the following ones to be bad.
# 
# You are given an API bool isBadVersion(version) which will return whether 
# version is bad. Implement a function to find the first bad version. 
# You should minimize the number of calls to the API. 

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# Linear Search (TLE)
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in xrange(1, n):
            if isBadVersion(i):
                return i 
        return n

# Binary search
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) / 2 # Prevent integer overflow (Though Python won't...)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1 # Prevent infinite loop
        return left
