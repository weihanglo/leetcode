#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/binary-tree-preorder-traversal/


# 1. Recursive
class Solution1(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        self.preorder(root, arr)
        return arr

    def preorder(self, node, arr):
        if node:
            arr.append(node.val)
            self.preorder(node.left, arr)
            self.preorder(node.right, arr)


# 2. Iterative
class Solution2(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                arr.append(node.val)  # Append before proceed to left node
                node = node.left
            else:
                n = stack.pop()
                node = n.right
        return arr


# 3. Another iterative solution. (Only append right node to stack)
class Solution3(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        stack = [root]
        while stack:
            node = stack.pop()
            while node:
                arr.append(node.val)
                if node.right:
                    stack.append(node.right)
                node = node.left
        return arr
