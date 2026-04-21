""""
Problem:
LeetCode 125 - Valid Palindrome

Pattern:
String Filtering + Reverse Comparison

Technique:
- Filter only alphanumeric characters
- Convert to lowercase
- Build cleaned string
- Compare with its reverse

Time Complexity Idea:
- O(n) time (scan + reverse)
- O(n) space (extra string)
"""

class Solution(object):
    def isPalindrome(self, s):
        newstr="".join(i.lower() for i in s if i.isalnum())
        return newstr==newstr[::-1]
