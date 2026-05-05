# Problem:
# Given a string s, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.

# Pattern:
# Two pointers

# Technique:
# - Clean string by keeping only alphanumeric characters
# - Convert to lowercase
# - Use two pointers from both ends
# - Compare characters and move inward

# Time complexity idea:
# O(n), where n is the length of the string
# Space complexity: O(n) due to cleaned string

class Solution(object):
    def isPalindrome(self, s):
        s = "".join(i.lower() for i in s if i.isalnum())
        
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
