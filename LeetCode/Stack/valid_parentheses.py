"""
Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Pattern:
Stack

Technique:
Use a stack to keep track of opening brackets.
- Push opening brackets onto the stack.
- When a closing bracket is encountered:
  - Check if the stack is empty. If yes, return False.
  - Verify that the top of the stack matches the corresponding opening bracket.
  - If it matches, pop from the stack; otherwise, return False.
- At the end, the stack should be empty for the string to be valid.

Time Complexity Idea:
- Traverse the string once.
- Each bracket is pushed and popped at most once.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack:
                    return False

                if stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
