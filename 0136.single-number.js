// Question: https://leetcode.com/problems/single-number
//
// Given an array of integers, every element appears twice except for one. 
// Find that single one.

// Note:
// Your algorithm should have a linear runtime complexity. 
// Could you implement it without using extra memory? 

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  const arr = nums.sort()
  if (arr.length < 2) {
    return arr[0]
  }
  for (let i = 1; i <= arr.length; i += 2) {
    if (arr[i - 1] != arr[i]) {
      return arr[i - 1]
    }
  }
};

