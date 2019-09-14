// Question: https://leetcode.com/problems/power-of-three/
//
// Given an integer, write a function to determine if it is a power of three.
//
// Example 1:
//
// ```
// Input: 27
// Output: true
// ```
//
// Follow up:
// Could you do it without using any loop / recursion?

/// Naive solution
impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {
        let mut x = n;
        if x > 1 {
            while x % 3 ==0 {
                x /= 3;
            }
        }
        x == 1
    }
}

/// Max power of 3 number within i32 range.
/// 3^20 > 2^(32 - 1) = 2147483648 > 3^19 = 1162261467
impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {
        n > 0 && 1162261467 % n == 0
    }
}
