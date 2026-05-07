# Problem:
# Given an integer array nums and an integer k,
# find a contiguous subarray of size k with the maximum average value.
# Return the maximum average.

# Pattern:
# Sliding Window (fixed size)

# Technique:
# - Compute sum of first k elements
# - Slide window by adding right element and removing left element
# - Track maximum sum seen
# - Divide final result by k to get average

# Time complexity idea:
# O(n), single pass over array
# Space complexity: O(1)

class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum
        left = 0

        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[left]
            left += 1

            max_sum = max(max_sum, window_sum)

        return float(max_sum) / k
