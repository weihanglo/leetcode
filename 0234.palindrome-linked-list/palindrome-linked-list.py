#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Question: https://leetcode.com/problems/palindrome-linked-list/
#
# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Use two pointer. The fast one moves two gaps in a leap. The other slower one 
# moves only one step. When the fast pointer finished its iteration. Stop the
# loop and the slow one would be on the half of the linked list. Then reverse
# second half list from slow pointer and iterate whole list from head and tail.
#
# Controversially, it may not esaily be seem as a O(n) space solution due to
# the nature of linked list use additionsl memeory when reversed a list.
# But if the value is more larger then pointers themself, we may ignore the
# memory comsuption of creating pointers.
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Move slow pointer to the middle of the list.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next # Leap two steps.
        # Reversed second half.
        pre_slow = None
        while slow:
            temp = slow.next
            slow.next = pre_slow
            pre_slow = slow
            slow = temp
        slow = pre_slow
        # Comparison
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True
