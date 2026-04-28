"""

Problem:
Given an integer array nums, find the subarray with the largest sum, and return both the sum and the subarray.

-- Pattern:
Dynamic Programming

-- Technique:
Kadane’s Algorithm (greedy running sum with reset point tracking)

-- Time Complexity:
O(n) — single pass

-- Space Complexity:
O(1) — constant extra space (excluding output subarray)

"""


class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        start = 0
        end = 0
        temp_start = 0

        for i in range(1, len(nums)):

            # decide whether to start new subarray or extend
            if nums[i] > current_sum + nums[i]:
                current_sum = nums[i]
                temp_start = i
            else:
                current_sum += nums[i]

            # update max and track indices
            if current_sum > max_sum:
                max_sum = current_sum
                start = temp_start
                end = i

        return max_sum, nums[start:end + 1]
