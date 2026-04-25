# Problem:
# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
# Do this in-place without making a copy of the array.

# Pattern:
# Scan → Decide → Write (in-place overwrite)

# Technique:
# First pass: move all non-zero elements forward.
# Second pass: fill remaining positions with 0.

# Time complexity:
# O(n) time, O(1) extra space

# Solution:

class Solution(object):
    def moveZeroes(self, nums):
        if not nums:
            return

        k = 0

        # Step 1: move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        # Step 2: fill remaining with zeros
        for i in range(k, len(nums)):
            nums[i] = 0
