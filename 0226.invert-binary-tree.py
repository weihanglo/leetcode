#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Question https://leetcode.com/problems/invert-binary-tree
# How to solve:
# Traverse all nodes, exchange their left node and right node.


# 1. DFS, iterative, pre-order traversal.
# This algorithm beats 100% Python solutions.
class Solution1(object):
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


# 2. DFS, recursive, pre-order traversal.
class Solution2(object):
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
