#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/


# 1. Recursive
class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        self.in_order(root, arr)
        return arr

    def in_order(self, node, arr):
        if not node:
            return
        self.in_order(node.left, arr)
        arr.append(node.val)
        self.in_order(node.right, arr)


# 2. Iterative
class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        stack = []
        node = root
        while node or stack:
            while node:  # Push all left nodes to stack.
                stack.append(node)
                node = node.left
            node = stack.pop()
            arr.append(node.val)  # Append after all left nodes.
            node = node.right
        return arr


# 3. Morris in-roder tree traversal.
#
# Core Concept: Append tree to right node of the rightmost node.
# Steps:
# 1. Initialize current as root
# 2. While current is not null
#   If current does not have left node
#     a. Get current's value (in-order)
#     b. Proceed to right node (current is right node now)
#   Else
#     a. Make current be the right node of rightmost node
#     b. Proceed to left node (current is right node now)
#
# Ref: https://stackoverflow.com/questions/5502916/
class Solution3(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        node = root
        while node:
            if not node.left:
                arr.append(node.val)
                node = node.right
            else:
                pre = node.left
                while pre.right:
                    pre = pre.right
                pre.right = node
                node = node.left
                pre.right.left = None  # Remove left tree to avoid infinite loop.
        return arr
