#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
#
# The flattened tree should look like:
#
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6


# 1. Bottom up, pre-order traversal.
class Solution1(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.flatten_helper(root, None)

    def flatten_helper(self, node, prev):
        if not node:
            return prev
        prev = self.flatten_helper(node.right, prev)
        prev = self.flatten_helper(node.left, prev)
        node.right = prev
        node.left = None
        return node
