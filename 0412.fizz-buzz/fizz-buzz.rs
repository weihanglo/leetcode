//  Write a program that outputs the string representation of numbers from 1 to n.
// 
//  But for multiples of three it should output “Fizz” instead of the number and
//  for the multiples of five output “Buzz”. For numbers which are multiples of
//  both three and five output “FizzBuzz”.
// 
//  Example:
// 
//  n = 15,
// 
//  Return:
//  [
//      "1",
//      "2",
//      "Fizz",
//      "4",
//      "Buzz",
//      "Fizz",
//      "7",
//      "8",
//      "Fizz",
//      "Buzz",
//      "11",
//      "Fizz",
//      "13",
//      "14",
//      "FizzBuzz"
//  ]

impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        (1..=n).map(|x| {
            match x {
                x if x % 15 == 0 => String::from("FizzBuzz"),
                x if x % 3 == 0 => String::from("Fizz"),
                x if x % 5 == 0 => String::from("Buzz"),
                _ => x.to_string(),
            }
        }).collect()
    }
}

impl Solution2 {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        (1..=n).map(|x| {
            let by3 = x % 3 == 0;
            let by5 = x % 5 == 0;
            match (by3, by5) {
                (true, true) => "FizzBuzz".into(),
                (true, false) => "Fizz".into(),
                (false, true) => "Buzz".into(),
                (false, false) => x.to_string(),
            }
        }).collect()
    }
}
