// Question: https://leetcode.com/problems/valid-palindrome/
//
// Given a string, determine if it is a palindrome, 
// considering only alphanumeric characters and ignoring cases.
//
// A palindrome is a word, phrase, number, or other sequence of characters which
// reads the same backward as forward, such as madam or "taco cat" or racecar.
//
// For example,
// "A man, a plan, a canal: Panama" is a palindrome.
// "race a car" is not a palindrome.
//
// Note:
// Have you consider that the string might be empty?
// This is a good question to ask during an interview.
//
// For the purpose of this problem, we define empty string as valid palindrome. 

// Use Regex to remove non-alnum characters. 
// With two pointer.
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
  const m = s.toLowerCase().match(/([a-z0-9]+)/g)
  if (!m) {
    return true
  }
  const charArray = m.join('').split('')
  let i = 0
  let j = charArray.length - 1
  while(i < j) {
    if (charArray[i] !== charArray[j]) {
      return false
    }
    i++
    j--
  }
  return true
};


// Two pointer only.
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
  let str = s.toLowerCase()
  let i = 0
  let j = str.length - 1
  const re = /[a-z0-9]/
  while (i < j) {
    while (i < j && !re.test(str[i])) {
      i++
    }
    while (i < j &&!re.test(str[j])) {
      j--
    }
    if (str[i] !== str[j]) {
      return false
    }
    i++
    j--
  }
  return true
}
