#You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

#Return the number of '*' in s, excluding the '*' between each pair of '|'.

#Note that each '|' will belong to exactly one pair.

class Solution(object):
    def countAsterisks(self, s):
        count = 0
        barCount = 0
        for i in s:
            if (i == '|'):
                barCount += 1

            if (barCount % 2 == 0) and i == '*':
                count += 1
        return count

result = Solution().countAsterisks("yo|uar|e**|b|e***au|tifu|l")
print(result)