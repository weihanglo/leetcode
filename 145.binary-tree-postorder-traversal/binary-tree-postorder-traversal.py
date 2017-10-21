#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/binary-tree-postorder-traversal/


# 1. Recursive
class Solution1(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        self.postorder(root, arr)
        return arr

    def postorder(self, node, arr):
        if node:
            self.postorder(node.left, arr)
            self.postorder(node.right, arr)
            arr.append(node.val)


# 2. Naïve iterative solution with deque.
class Solution2(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                arr.append(node.val)
        return arr[::-1]


# 3. Two pointer without reversed. O(n) time and O(n) space complexity.
class Solution3(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        stack = []
        node = root
        last_node = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            top_node = stack[-1]
            if top_node.right and last_node is not top_node.right:
                node = top_node.right
            else:
                arr.append(top_node.val)
                last_node = stack.pop()  # == top_node
        return arr
