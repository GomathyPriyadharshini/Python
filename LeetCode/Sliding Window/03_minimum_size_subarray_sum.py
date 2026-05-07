# Problem:
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray
# whose sum is greater than or equal to target.
# If no such subarray exists, return 0.

# Pattern:
# Sliding Window (variable size)

# Technique:
# - Expand window using right pointer
# - Keep adding elements to current sum
# - Shrink window from left while sum >= target
# - Track minimum valid window length

# Time complexity idea:
# O(n), each element is visited at most twice
# Space complexity: O(1)

class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        min_length = float('inf')
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length
