#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/binary-tree-paths/
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]


# 1. Simple DFS without string builder.
# Ref: https://discuss.leetcode.com/topic/21559
class Solution1(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result = []
        stack = [(root, '')]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                result.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + '->'))
            if node.left:
                stack.append((node.left, ls + str(node.val) + '->'))
        return result


# 2. DSF solution.
# No string concatenation overhead (but introduce set searching overhead).
class Solution2(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        stack = []
        node = root
        seen = set()
        while stack or node:
            while node and node not in seen:
                stack.append(node)
                node = node.left
            node = stack[-1] if stack else None
            if not node:
                continue
            if not node.left and not node.right:
                result.append('->'.join(str(x.val) for x in stack))
                seen.add(node)
                stack.pop()
                continue
            if node.right and node.right not in seen:
                node = node.right
            elif stack:
                seen.add(stack.pop())
        return result
