// Question: https://leetcode.com/problems/contains-duplicate/
//
// Given an array of integers, find if the array contains any duplicates.
// Your function should return true if any value appears at least twice
// in the array, and it should return false if every element is distinct.

// 1. O(n) time, O(n) space
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  const set = new Set()
  for (let num of nums) {
    if (set.has(num)) {
      return true
    }
    set.add(num)
  }
  return false
};


// 2. Sort the array in advance.
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  const arr = nums.sort()
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] === arr[i - 1]) {
      return true
    }
  }
  return false
};
