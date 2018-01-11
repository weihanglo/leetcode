// Question: https://leetcode.com/problems/two-sum/
//
// Given an array of integers, return indices of the two numbers 
// such that they add up to a specific target.
//
// You may assume that each input would have exactly one solution, 
// and you may not use the same element twice.
//
// Example:
//
// Given nums = [2, 7, 11, 15], target = 9,
// 
// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

// 1. naive implementation. O(n^2) time, O(1) space.
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  for (let [i, v0] of nums.entries()) {
    for (let [j, v1] of nums.entries()) {
      if (i !== j && v0 + v1 === target) {
        return [i, j]
      }
    }
  }
};

// 2. Use hashmap to store index. O(n) time, O(n) space.
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  const map = new Map()
  for (let [idx, val] of nums.entries()) {
    const index = map.get(target - val)
    if (typeof index !== 'undefined') {
      return [index, idx]
    }
    map.set(val, idx)
  }
  return []
};
