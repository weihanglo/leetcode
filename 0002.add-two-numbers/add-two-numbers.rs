// Problem: https://leetcode.com/problems/add-two-numbers/
//
// You are given two non-empty linked lists representing two non-negative
// integers. The digits are stored in reverse order and each of their nodes
// contain a single digit. Add the two numbers and return it as a linked list.
//
// You may assume the two numbers do not contain any leading zero, except the
// number 0 itself.
//
// Example:
//
// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut node = Box::new(ListNode::new(0));
        let mut head = &mut node;
        let mut l_node = l1;
        let mut r_node = l2;
        let mut overflow = 0;

        while l_node.is_some() || r_node.is_some() {
            let sum = l_node.clone()
                .map(|l| {
                    l_node = l.next;
                    l.val
                }).unwrap_or_default() +
                r_node.clone().map(|r| {
                    r_node = r.next;
                    r.val
                }).unwrap_or_default() +
                overflow;
            head.next = Some(Box::new(ListNode::new(sum % 10)));
            overflow = sum / 10;
            head = head.next.as_mut().unwrap();
        }

        if overflow > 0 {
            head.next = Some(Box::new(ListNode::new(overflow % 10)));
        }

        node.next
    }
}
