"""
Problem Statement:
You are climbing a staircase.
It takes n steps to reach the top.

Each time you can either climb:
- 1 step
- 2 steps

Return the number of distinct ways to climb to the top.

Pattern:
Dynamic Programming / Fibonacci Pattern

Technique:
- The number of ways to reach step n depends on:
    ways(n-1) + ways(n-2)
- Use two variables to optimize space usage

Time complexity idea:
- O(n) time
- O(1) space
"""

class Solution(object):

    def climbStairs(self, n):

        if n <= 2:
            return n

        a, b = 1, 2

        for _ in range(3, n + 1):
            a, b = b, a + b

        return b
