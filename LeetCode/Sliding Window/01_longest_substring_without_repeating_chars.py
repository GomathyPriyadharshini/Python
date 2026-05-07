# Problem:
# Given a string s, find the length of the longest substring
# without duplicate characters.

# Pattern:
# Sliding Window + HashSet

# Technique:
# - Use two pointers (left, right) to maintain a window
# - Expand right pointer and add characters to a set
# - If duplicate found, shrink window from left until valid
# - Track maximum window size

# Time complexity idea:
# O(n), each character is added and removed at most once
# Space complexity: O(min(n, charset size))

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_len = 0
        window = set()

        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
