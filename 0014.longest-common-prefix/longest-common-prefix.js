// Question: https://leetcode.com/problems/longest-common-prefix/
//
// Write a function to find the longest common prefix string 
// amongst an array of strings. 

// 1. Horizontal scanning
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
  let prefix = str[0] || ''
  for (let str of strs) {
    while (str.indexOf(prefix) !== 0) {
      prefix = prefix.slice(0, -1)
    }
  }
  return prefix
};
