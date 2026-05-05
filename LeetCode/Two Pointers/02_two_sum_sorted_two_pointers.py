# Problem:
# Given a 1-indexed sorted array, find two numbers such that they add up to a target.
# Return their indices (1-based). Exactly one solution exists.
# Cannot use the same element twice and must use constant extra space.

# Pattern:
# Two pointers

# Technique:
# - Use two pointers: one at the start, one at the end
# - If sum is too small → move left pointer forward
# - If sum is too large → move right pointer backward
# - If equal → return indices (1-based)

# Time complexity idea:
# O(n), single pass
# Space complexity: O(1)

class Solution(object):
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers) - 1
        
        while i < j:
            current_sum = numbers[i] + numbers[j]
            
            if current_sum == target:
                return [i + 1, j + 1]
            elif current_sum < target:
                i += 1
            else:
                j -= 1
