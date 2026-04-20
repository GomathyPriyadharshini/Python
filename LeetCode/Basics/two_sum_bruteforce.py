# Problem:
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# Assume exactly one solution exists and same element cannot be reused.

# Pattern: Brute Force Search
# Technique: Nested loops to check all pairs
# Time complexity idea: O(n^2)

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))
