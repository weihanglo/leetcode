// Question: https://leetcode.com/problems/ugly-number/
//
// Write a program to check whether a given number is an ugly number.
//
// Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
// For example, 6, 8 are ugly while 14 is not ugly since it includes another
// prime factor 7.
//
// Note that 1 is typically treated as an ugly number.

// Just a variation of fibonacci sequence. Use dynamic programming to solve it.

/**
 * @param {number} num
 * @return {boolean}
 */
var isUgly = function(num) {
  if (!num) {
    return false
  }
  const factor = (num, f) => {
    while (true) {
      let temp = num % f
      if (temp !== 0 || num === 1) {
          break
      }
      num /= f
    }
    return num
  }
  const two = factor(num, 2)
  const three = factor(two, 3)
  const five = factor(three, 5)
  return five === 1
};
