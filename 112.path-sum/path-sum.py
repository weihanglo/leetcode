#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/path-sum/
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# For example:
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
#
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


# 1. Recursive
class Solution1(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum - root.val) or \
            self.hasPathSum(root.right, sum - root.val)


# 2. DFS, interative solution (post order).
class Solution2(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        stack = []
        node = root
        previous_node = None
        current_sum = 0
        while stack or node:
            while node:  # Visit all left nodes
                stack.append(node)
                current_sum += node.val
                node = node.left
            node = stack[-1]
            if not node.left and not node.right and current_sum == sum:
                return True
            if node.right and node.right is not previous_node:
                # Visit right tree and compare to previous node.
                node = node.right
            else:
                previous_node = node
                current_sum -= node.val
                stack.pop()  # Continue popping to parent
                node = None
        return False
