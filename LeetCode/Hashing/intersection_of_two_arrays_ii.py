"""
Problem:
Given two integer arrays nums1 and nums2, return their intersection where each element appears as many times as it shows in both arrays.

-- Pattern:
Hash Map / Frequency Counting

-- Technique:
Use dictionary (or Counter) to track frequencies and match elements greedily

-- Time Complexity:
O(n + m)

-- Space Complexity:
O(min(n, m))

"""


from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        return list((Counter(nums1) & Counter(nums2)).elements())
