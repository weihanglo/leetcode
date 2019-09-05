/// Question: https://leetcode.com/problems/integer-to-roman/
///
/// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
///
/// Symbol       Value
/// I             1
/// V             5
/// X             10
/// L             50
/// C             100
/// D             500
/// M             1000
///
/// For example, two is written as II in Roman numeral, just two one's added 
/// together. Twelve is written as, XII, which is simply X + II. The number 
/// twenty seven is written as XXVII, which is XX + V + II.
///
/// Roman numerals are usually written largest to smallest from left to right. 
/// However, the numeral for four is not IIII. Instead, the number four is 
/// written as IV. Because the one is before the five we subtract it making 
/// four. The same principle applies to the number nine, which is written as 
/// IX. There are six instances where subtraction is used:
///
///     I can be placed before V (5) and X (10) to make 4 and 9. 
///     X can be placed before L (50) and C (100) to make 40 and 90. 
///     C can be placed before D (500) and M (1000) to make 400 and 900.
///
/// Given an integer, convert it to a roman numeral. Input is guaranteed to be 
/// within the range from 1 to 3999.
///
impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        let mut remainder = num;
        NUMS.iter().zip(LITERALS.iter()).fold(
            String::new(), 
            |mut acc, (divisor, roman)| {
                let quotient = remainder / divisor;
                if quotient > 0 {
                    remainder %= divisor * quotient;
                    acc.push_str(&roman.repeat(quotient as usize));
                }
                acc
            }
        )
    }
}

const LITERALS: [&str; 13] = [
    "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
];
const NUMS: [i32; 13] = [
    1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
];
