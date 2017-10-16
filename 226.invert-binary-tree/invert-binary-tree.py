#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Question https://leetcode.com/problems/invert-binary-tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# How to solve:
# Traverse all nodes, exchange their left node and right node.

# DFS. Iterative. Pre-order traversal.
# This algorithm beats 100% Python solutions.
def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
    return root

# DFS. Recursive. Pre-order traversal.
def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root:
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root
