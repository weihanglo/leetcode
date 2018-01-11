// Question: https://leetcode.com/problems/move-zeroes/
//
// Given an array nums, write a function to move all 0's to the end of it
// while maintaining the relative order of the non-zero elements.
//
// For example, given nums = [0, 1, 0, 3, 12], after calling your function,
// nums should be [1, 3, 12, 0, 0].
//
// Note:
//   1. You must do this in-place without making a copy of the array.
//   2. Minimize the total number of operations.

// 1. Naive implementation. O(n) time, O(n) space.
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
  const arr = []
  for (let num of nums) {
    num && arr.push(num)
  }
  while (arr.length < nums.length) {
    arr.push(0)
  }
  for (let [i, v] of arr.entries()) {
    nums[i] = v
  }
};

// 2. Last non zero index flag. O(n) time, O(1) space.
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
  let nonZeroIndex = 0
  for (let [i, num] of nums.entries()) {
    if (num !== 0) {
      nums[nonZeroIndex] = num
      nonZeroIndex++
    }
  }
  for (let i = nonZeroIndex; i < nums.length; i++) {
    nums[i] = 0
  }
};

// 3. Swap Last non zero element and zeroes.
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
  let nonZeroIndex = 0
  for (let [i, num] of nums.entries()) {
    if (num !== 0) {
      nums[i] = nums[nonZeroIndex]
      nums[nonZeroIndex] = num
      nonZeroIndex++
    }
  }
};
