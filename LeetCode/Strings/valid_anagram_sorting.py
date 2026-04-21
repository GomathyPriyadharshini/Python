"""
Problem:
LeetCode 242 - Valid Anagram

Pattern:
Sorting / String Comparison

Technique:
- Convert strings into sorted form
- Compare sorted results
- If equal → anagram

Time Complexity Idea:
- O(n log n) due to sorting
- O(n) space for sorted output
"""

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
