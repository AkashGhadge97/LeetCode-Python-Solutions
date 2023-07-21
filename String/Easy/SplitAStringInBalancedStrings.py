# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

class Solution(object):
    def balancedStringSplit(self, s):
        count = 0
        final = 0
        for i in s:
            if i == 'L':
                count += 1
            if i == 'R':
                count -= 1
            if count == 0:
                final += 1
        return final


result = Solution().balancedStringSplit("RLRRRLLRLL")
print(result)
