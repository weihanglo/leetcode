# Question: https://leetcode.com/problems/climbing-stairs
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.

# Just a variation of fibonacci sequence. Use dynamic programming to solve it.
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
          return n
        first = 1
        second = 2
        i = 2
        while i < n:
          second, first = second + first, second
          i += 1
        return second
