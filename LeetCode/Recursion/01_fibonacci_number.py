"""
Problem Statement:
Given n calculate the nth Fibonacci number.

F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2), for n > 1

Pattern:
Dynamic Programming / Recursion Optimization

Technique:
- Memoization (top-down DP)
- Iterative (bottom-up DP)

Time complexity idea:
- Naive recursion: O(2^n)
- Memoization: O(n)
- Iterative: O(n) time, O(1) space
"""

class Solution(object):

    # Optimized solution (recommended)
    def fib(self, n):
        if n <= 1:
            return n

        a, b = 0, 1

        for i in range(n):
            a, b = b, a + b

        return a


    # Alternative: Memoization approach
    def fib_memo(self, n, memo=None):
        if memo is None:
            memo = {}

        if n in memo:
            return memo[n]

        if n <= 1:
            return n

        memo[n] = self.fib_memo(n - 1, memo) + self.fib_memo(n - 2, memo)
        return memo[n]
