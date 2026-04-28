"""
Problem:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

-- Pattern:
Dynamic Programming

-- Technique:
Kadane’s Algorithm (greedy + running sum reset when negative)

-- Time Complexity:
O(n) — single pass through the array

-- Space Complexity:
O(1) — constant extra space
"""

class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], nums[i] + current_sum)
            max_sum = max(max_sum, current_sum)

        return max_sum
