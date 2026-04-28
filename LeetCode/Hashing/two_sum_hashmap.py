"""
Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

-- Pattern:
Hash Map Lookup

-- Technique:
Store value → index and check for complement while iterating

-- Time Complexity:
O(n)

-- Space Complexity:
O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        vals = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in vals:
                return [vals[need], i]

            vals[num] = i


# Example usage
obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))
