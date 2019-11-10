/// Question: https://leetcode.com/problems/isomorphic-strings/
///
/// Given two strings `s` and `t`, determine if they are isomorphic.
///
/// Two strings are isomorphic if the characters in s can be replaced to get `t`.
///
/// All occurrences of a character must be replaced with another character
/// while preserving the order of characters. No two characters may map to the
/// same character but a character may map to itself.
///
/// Example 1:
///
/// ```
/// Input: s = "egg", t = "add"
/// Output: true
/// ```
impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        use std::collections::HashMap;
        if s.len() != t.len() {
            return false;
        }
        let mut s2t = HashMap::new();
        let mut t2s = HashMap::new();
        for (c0, c1) in s.chars().zip(t.chars()) {
            
            let s = s2t.entry(c1).or_insert(c0);
            let t = t2s.entry(c0).or_insert(c1);
            if *s != c0 || *t != c1 {
                return false;
            }
        }

        true
    }
}
