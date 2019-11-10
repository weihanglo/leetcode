#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal
#
# Given a binary tree, return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# return its level order traversal as:
# 
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# 1. Intuitive level-order traversal solution.
class Solution1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        queue = []
        queue.append(root)
        while queue:
            nodes = []
            for _ in xrange(len(queue)):
                node = queue.pop(0)
                nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(nodes)
        return result


# 2. Use pre-order traversal to construct tree levels.
# Here we got an pre-order list helper.
# Beats 95% Python solutions.
class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []

        def pre_order_helper(node, depth):
            if not node:
                return
            if len(ret) == depth:
                ret.append([])
            ret[depth].append(node.val)
            pre_order_helper(node.left, depth + 1)
            pre_order_helper(node.right, depth + 1)

        pre_order_helper(root, 0)
        return ret
