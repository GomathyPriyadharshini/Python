# Problem:
# Convert a Roman numeral string to an integer.

# Pattern: HashMap + Lookahead comparison
# Technique: Compare current and previous characters to decide add/subtract
# Time complexity idea: O(n)

class Solution(object):
    def romanToInt(self, s):
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100,
            "D": 500, "M": 1000
        }

        num = 0

        for i in range(1, len(s)):
            if roman[s[i]] > roman[s[i - 1]]:
                num -= roman[s[i - 1]]
            else:
                num += roman[s[i - 1]]

        num += roman[s[-1]]
        return num


obj = Solution()
print(obj.romanToInt("III"))
