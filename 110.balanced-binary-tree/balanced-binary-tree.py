#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/balanced-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. DFS, recursive, bottom-up solution.
# Calculate height of subtrees, if any subtree is not balanced. We do an early
# return instead of check every nodes. We check height from the bottom of the
# whole tree. Each node would only access only one time, so the time complexity
# is O(n). That's why the algorithm is a bottom-up solution.
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.get_height(root) != None
    def get_height(self, root):
        if not root:
            return 0
        left = self.get_height(root.left)
        if left == None:
            return left
        right = self.get_height(root.right)
        if right == None:
            return right
        if abs(left - right) > 1:
            return None
        return max(left, right) + 1
