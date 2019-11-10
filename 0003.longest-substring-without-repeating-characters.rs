/// Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/
///
/// Given a string, find the length of the longest substring without repeating characters.
///
/// Example 1:
///
/// ```
/// Input: "aabaab!bb"
/// Output: 3 
/// Explanation: The answer is "ab!", with the length of 3. 
/// ```
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut map = std::collections::HashMap::new();
        let mut start = 0;
        let mut result = 0;
        for (i, c) in s.chars().enumerate() {
            map.entry(c)
                .and_modify(|x| {
                    start = start.max(*x + 1);
                    *x = i;
                })
                .or_insert(i);
            result = result.max(i - start + 1);
        }
        result as i32
    }
}
