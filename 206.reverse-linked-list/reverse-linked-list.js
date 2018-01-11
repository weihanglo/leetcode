// Question: https://leetcode.com/problems/reverse-linked-list/
//
// Reverse a singly linked list.
// 
// Hint:
// A linked list can be reversed either iteratively or recursively. 
// Could you implement both?

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

// 1. Recursive
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  if (!head || !head.next) {
    return head
  }
  const node = reverseList(head.next)
  head.next.next = head
  head.next = null
  return node
};

// 2. Iterative
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  let previous = null
  while (head) {
    const temp = head.next
    head.next = previous
    previous = head
    head = temp
  }
  return previous
};
