# Problem:
# Given an integer array nums and a value val,
# remove all occurrences of val in-place and return k,
# where k is the number of remaining elements.

# Pattern:
# Scan → Decide → Write (in-place overwrite)

# Technique:
# Use a write pointer (k) to store only valid elements
# while scanning the array.

# Time complexity:
# O(n) time, O(1) extra space

# Solution:

class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
