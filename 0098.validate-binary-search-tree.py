#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question: https://leetcode.com/problems/validate-binary-search-tree/
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#   - The left subtree of a node contains only nodes with keys less than
#     the node's key.
#   - The right subtree of a node contains only nodes with keys greater than 
#     the node's key.
#   - Both the left and right subtrees must also be binary search trees.
# Example 1:
# 
#     2
#    / \
#   1   3
# 
# Binary tree [2,1,3], return true.
# 
# Example 2:
# 
#     1
#    / \
#   2   3
# 
# Binary tree [1,2,3], return false. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def bst_validator(node, min_val, max_val):
            if not node:
                return True
            min_invalid = min_val != None and node.val <= min_val
            max_invalid = max_val != None and node.val >= max_val
            if min_invalid or max_invalid:
                return False
            return bst_validator(node.left, min_val, node.val) and \
                bst_validator(node.right, node.val, max_val)
        return bst_validator(root, None, None)

# Iterative. In-order.
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = []
        prev_node = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev_node and root.val <= prev_node.val:
                return False
            prev_node = root
            root = root.right
        return True
