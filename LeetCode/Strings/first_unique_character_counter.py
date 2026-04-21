"""
Problem:
LeetCode 387 - First Unique Character in a String

Pattern:
Hashmap / Frequency Counting

Technique:
- Use Counter to store frequency of each character
- Iterate string from left to right
- Return first index where frequency is 1

Time Complexity Idea:
- O(n) to build frequency map
- O(n) to scan string
- Overall: O(n)

"""

from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        freq = Counter(s)

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1
