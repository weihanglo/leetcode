#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree


# 1. Breadth-first-search, iterative, level-order solution.
class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if not root:
            return depth
        queue = []
        queue.append(root)
        while queue:
            depth += 1
            for _ in xrange(len(queue)):
                node = queue.pop(0)  # Dequeue first element.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


# 2. Depth-first-search, iterative solution.
class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if not root:
            return depth
        stack = []
        value = []
        stack.append(root)
        value.append(depth + 1)
        while stack:
            node = stack.pop()
            temp = value.pop()
            depth = max(temp, depth)
            if node.right:
                # We want to pop left node first while searching,
                # so append right first (stack is LIFO).
                stack.append(node.right)
                value.append(temp + 1)
            if node.left:
                stack.append(node.left)
                value.append(temp + 1)
        return depth


# 3. Depth-first-search, recursive solution.
class Solution3(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
