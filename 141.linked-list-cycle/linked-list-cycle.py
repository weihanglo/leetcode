#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Question: https://leetcode.com/problems/linked-list-cycle/
#
# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space? 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Hash set. O(n) space.
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

# Two pointers approach. One move fast, the other move slow. Eventually the two
# pointers would meet each other.
#
# Ref: leetcode official accepted solution
# https://leetcode.com/problems/linked-list-cycle/solution/
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = head.next
        while slow is not fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
