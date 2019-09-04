// Question: https://leetcode.com/problems/first-unique-character-in-a-string/
//
// Given a string, find the first non-repeating character in it and return
// it's index. If it doesn't exist, return -1.
//
// Examples:
//
// s = "leetcode"
// return 0.
//
// s = "loveleetcode",
// return 2.
//
// Note: You may assume the string contain only lowercase letters. 


// 1. Naive built-in method.
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
  const map = new Map()
  for (let i = 0; i < s.length; i++) {
    const char = s[i]
    if (s.indexOf(char) === s.lastIndexOf(char)) {
      return i
    }
  }
  return -1
};

// 2. Hash map. O(n) time, O(n) space.
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
  const map = new Map()
  for (let i = 0; i < s.length; i++) {
    const char = s[i]
    map.has(char)
      ? map.set(char, 2)
      : map.set(char, 1)
  }
  for (let i = 0; i < s.length; i++) {
    if (map.get(s[i]) === 1) {
      return i
    }
  }
  return -1
};
