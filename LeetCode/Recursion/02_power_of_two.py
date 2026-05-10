"""
Problem Statement:
Given an integer n, return true if it is a power of two.
Otherwise, return false.

An integer n is a power of two if there exists an integer x such that:
n == 2^x

Pattern:
Recursion + Divide by 2

Technique:
- Handle base cases for 0 and 1
- If n is odd (except 1), return False
- Recursively divide by 2 until reaching 1

Time complexity idea:
- O(log n)
- Since n is divided by 2 in each recursive call
"""

class Solution(object):
    def isPowerOfTwo(self, n):

        if n == 0:
            return False

        if n == 1:
            return True

        if n % 2 != 0:
            return False

        return self.isPowerOfTwo(n // 2)
