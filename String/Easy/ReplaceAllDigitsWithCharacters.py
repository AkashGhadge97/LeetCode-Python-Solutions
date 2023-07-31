# You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

# There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

class Solution(object):
    def replaceDigits(self, s):
        result = ''
        for i in range(0, len(s)):
            if (i % 2 == 0):
                result += s[i]
            else:
                result += chr(ord(s[i-1]) + int(s[i]))

        return result


result = Solution().replaceDigits("a1b2c3d4e")
print(result)
