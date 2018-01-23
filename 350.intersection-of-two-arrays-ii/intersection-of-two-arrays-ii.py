#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question: https://leetcode.com/problems/intersection-of-two-arrays-ii
#
# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Note:
#
#   - Each element in the result should appear as many times as it shows
#     in both arrays.
#   - The result can be in any order.
#
# Follow up:
#
#   - What if the given array is already sorted?
#     How would you optimize your algorithm?
#   - What if nums1's size is small compared to nums2's size?
#     Which algorithm is better?
#   - What if elements of nums2 are stored on disk, and the memory is limited
#     such that you cannot load all elements into the memory at once?

# Sort array first, then use two pointers.
# The underlying sorting algorithm is Timsort in Python 3, 
# so the best time complexity is O(n log n).
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        nums1.sort()
        nums2.sort()
        len1 = len(nums1)
        len2 = len(nums2)
        i = j = 0
        while i < len1 and j < len2:
            n1 = nums1[i]
            n2 = nums2[j]
            if n1 == n2:
                result.append(n1)
                i += 1
                j += 1
            elif n1 < n2:
                i += 1
            else:
                j += 1
        return result

# Hashmap. O(max(m, n)) time. O(max(m, n)) space.
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        result = []
        for n in nums1:
            if hashmap.get(n) == None:
                hashmap[n] = 1 
            else: 
                hashmap[n] += 1
        for n in nums2:
            el = hashmap.get(n)
            if el and el > 0:
                result.append(n)
                hashmap[n] -= 1
        return result
