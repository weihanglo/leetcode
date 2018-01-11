// Question: https://leetcode.com/problems/valid-anagram/
//
// Given two strings s and t, write a function to determine
// if t is an anagram of s.
//
// For example,
// s = "anagram", t = "nagaram", return true.
// s = "rat", t = "car", return false.
//
// Note:
// You may assume the string contains only lowercase alphabets.
//
// Follow up:
// What if the inputs contain unicode characters?
// How would you adapt your solution to such case?

// Sort strings to compare. 
// Time: O(n log n) if sort algo is implemented in O(n log n) time.
// Space: O(1) if sort algo is implemented in O(1) space.
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
  if (s.length !== t.length) {
    return false
  }
  const str0 = s.split('').sort()
  const str1 = t.split('').sort()
  for (let i = 0; i < str0.length; i++) {
    if (str0[i] !== str1[i]) {
      return false
    }
  }
  return true
};
