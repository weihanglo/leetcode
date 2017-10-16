#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question: https://leetcode.com/problems/maximum-binary-tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Ref: https://discuss.leetcode.com/topic/98509
def constructMaximumBinaryTree(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    stack = []
    for num in nums:
        node = TreeNode(num)
        while stack and stack[-1].val < num:
            node.left = stack.pop()
        if stack:
            stack[-1].right = node
        stack.append(node)
    return stack[0]
