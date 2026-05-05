# Problem:
# Reverse a string given as an array of characters in-place.
# Must use O(1) extra memory.

# Pattern:
# Two pointers

# Technique:
# - Use two pointers: one at the start, one at the end
# - Swap elements and move pointers inward
# - Continue until pointers meet

# Time complexity idea:
# O(n), where n is the length of the array
# Space complexity: O(1), in-place swaps

class Solution(object):
    def reverseString(self, s):
        i, j = 0, len(s) - 1
        
        while i < j:
            s[i], s[j] = s[j], s[i]  # swap
            i += 1
            j -= 1
