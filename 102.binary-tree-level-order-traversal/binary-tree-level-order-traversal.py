#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. Intuitive level-order traversal solution.
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
