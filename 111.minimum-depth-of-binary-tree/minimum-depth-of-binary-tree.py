#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/minimum-depth-of-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# To find the minimal path to nearest leaf node.  We should use breadth-first 
# (level-order) traversal solution to avoid traversing all nodes. Level-order 
# traversal means we would first search all nodes in current level before 
# enter next level.
# 
# This solution beats 95% python solutions using DFS-like recursive method.
def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    depth = 0
    if not root:
        return 0
    # This queue only contains child nodes of a certain parent node at a time.
    # That is to say, the length of the queue can only be 0, 1, or 2.
    queue = [] 
    queue.append(root)
    while queue:
        depth += 1
        for _ in xrange(len(queue)):
            # Loop all child nodes before visiting next node.
            node = queue.pop(0)
            if not node.left and not node.right:
                # It's a leaf. Return it directly!
                return depth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth

