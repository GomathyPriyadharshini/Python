# Problem:
# Check whether a given integer is a palindrome.

# Pattern: String conversion + reverse check
# Technique: Compare string with its reverse
# Time complexity idea: O(n)

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        return str(x) == str(x)[::-1]


obj = Solution()
print(obj.isPalindrome(121))
