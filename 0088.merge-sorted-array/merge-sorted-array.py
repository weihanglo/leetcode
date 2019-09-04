#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/merge-sorted-array/
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as 
# one sorted array.
#
# Note:
# You may assume that nums1 has enough space (size that is greater or 
# equal to m + n) to hold additional elements from nums2. The number of 
# elements initialized in nums1 and nums2 are m and n respectively.

# Via Leetcode discussion.
# Note: nums1 is a m + n length array. Don't worry about index out of bounds.
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
                # nums2[n - 1] is in its final place.
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                # Move nums[m - 1] to its final place.
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
