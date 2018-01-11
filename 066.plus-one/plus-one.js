// Question: https://leetcode.com/problems/plus-one/
//
// Given a non-negative integer represented as a non-empty array of digits,
// plus one to the integer.
//
// You may assume the integer do not contain any leading zero, except the
// number 0 itself.
//
// The digits are stored such that the most significant digit is at the head
// of the list.

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
  for (var i = digits.length - 1; i >= 0; i--) {
    if (digits[i] === 9) {
      digits[i] = 0
    } else {
      digits[i]++
      break
    }
  }
  if (digits[0] === 0) {
    digits.unshift(1)
  }
  return digits
};
