# Problem:
# Given a sorted integer array nums, remove duplicates in-place such that
# each unique element appears at most twice.
# Return k such that first k elements contain the valid result.

# Pattern:
# Scan → Decide → Write (in-place overwrite)

# Technique:
# Since array is sorted, duplicates are adjacent.
# Allow at most 2 occurrences by comparing current element
# with the element at position k-2.

# Time complexity:
# O(n) time, O(1) extra space

# Solution:

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        k = 2  # first two elements are always allowed

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k
