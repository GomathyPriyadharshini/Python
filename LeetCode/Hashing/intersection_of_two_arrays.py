"""
Problem:
Return the unique intersection of two integer arrays.

-- Pattern:
Hash Set / Set Operations

-- Technique:
Convert arrays to sets and use set intersection

-- Time Complexity:
O(n + m)

-- Space Complexity:
O(n + m)
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
