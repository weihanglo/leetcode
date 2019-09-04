#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Question: https://leetcode.com/problems/average-of-levels-in-binary-tree

# Given a non-empty binary tree, return the average value of the nodes
# on each level in the form of an array.
#
# Example 1:
#
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
#
# Explanation:
# The average value of nodes on level 0 is 3, on level 1 is 14.5,
# and on level 2 is 11. Hence return [3, 14.5, 11].
#
# Note:
#
#     The range of node's value is in the range of 32-bit signed integer.


# 1. Simple level-order traversal.
class Solution1:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        stack = [root]
        while stack:
            new_stack = []
            value = 0.0
            length = len(stack)
            while stack:
                node = stack.pop()
                value += node.val
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            result.append(value / length)
            stack = new_stack
        return result


# 2. Depth first search.
class Solution2(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []

        def pre_order_helper(node, depth):
            if not node:
                return
            if len(result) == depth:
                result.append([0, 0])
            result[depth][0] += node.val
            result[depth][1] += 1
            pre_order_helper(node.left, depth + 1)
            pre_order_helper(node.right, depth + 1)
        pre_order_helper(root, 0)
        return [sum / float(count) for sum, count in result]
