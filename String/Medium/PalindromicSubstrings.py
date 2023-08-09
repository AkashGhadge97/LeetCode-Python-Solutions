# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

class Solution(object):
    def countSubstrings(self, s):
        lst = []
        for i in range(0, len(s)):
            for j in range(0, len(s)+1):
                if (s[i:j] != ''):
                    lst.append(s[i:j])
        count = 0
        for i in lst:
            if (i[::-1] == i):
                count += 1
        return count
