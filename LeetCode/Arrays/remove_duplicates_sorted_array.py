# Problem:
# Given a sorted integer array nums, remove duplicates in-place such that
# each element appears only once and return the number of unique elements (k).
# The first k elements of nums should contain the unique values in order.

# Pattern:
# Scan + overwrite (two-pointer style)

# Technique:
# Use one pointer (i) to scan the array and another pointer (k)
# to track the position of the next unique element.

# Time complexity idea:
# O(n) time, O(1) extra space

# Solution:

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1  # position to place next unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
