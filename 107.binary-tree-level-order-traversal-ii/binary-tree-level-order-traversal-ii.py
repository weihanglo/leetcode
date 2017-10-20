#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal-ii
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. Reversed level-order traversal solution.
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        queue = [root]
        while queue:
            nodes = []
            for node in xrange(len(queue)):
                node = queue.pop(0)
                if node:
                    nodes.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if nodes:
                result.append(nodes)
        result.reverse()
        return result

# 2. Level-order traversal solution with `collections.deque`.
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = deque()
        queue = [root]
        while queue:
            nodes = []
            for node in xrange(len(queue)):
                node = queue.pop(0)
                if node:
                    nodes.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if nodes:
                result.appendleft(nodes)
        return list(result)


