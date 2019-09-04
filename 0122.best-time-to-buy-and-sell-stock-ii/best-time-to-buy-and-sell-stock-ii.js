// Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
//
// Say you have an array for which the ith element is the price of
// a given stock on day i.
//
// Design an algorithm to find the maximum profit.
// You may complete as many transactions as you like
// (ie, buy one and sell one share of the stock multiple times).
// However, you may not engage in multiple transactions at the same time
// (ie, you must sell the stock before you buy again).

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  let profit = 0
  for (let i = 0; i < prices.length - 1; i++) {
    profit += Math.max(prices[i + 1] - prices[i], 0)
  }
  return profit
};
