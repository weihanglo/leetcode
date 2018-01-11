// Question: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
//
// Given a linked list, remove the nth node from the end of list and
// return its head.
//
// For example,
//
//    Given linked list: 1->2->3->4->5, and n = 2.
//
//    After removing the second node from the end,
//    the linked list becomes 1->2->3->5.
//
// Note:
// Given n will always be valid.
// Try to do this in one pass. 

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

// Maintain the gap between first and second pointer.
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
  const prehead = new ListNode(-1)
  prehead.next = head
  let first = prehead
  let second = prehead
  for (let i = 0; i <= n; i++) {
    first = first.next
  }
  // Now there is a n-node gap between first and second pointers.
  while (first) {
    first = first.next
    second = second.next
  }
  second.next = second.next.next
  return prehead.next
};
