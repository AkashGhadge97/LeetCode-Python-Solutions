# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

class Solution(object):
    def halvesAreAlike(self, s):
        partOne = s[0:int(len(s)/2)]
        partTwo = s[int(len(s)/2):]
        countPartOne = 0
        countPartTwo = 0
        for i, j in zip(partOne, partTwo):
            if ((i == 'a' or i == 'A') or (i == 'e' or i == 'E') or (i == 'i' or i == 'I') or (i == 'o' or i == 'O') or (i == 'u' or i == 'U')):
                countPartOne += 1
            if ((j == 'a' or j == 'A') or (j == 'e' or j == 'E') or (j == 'i' or j == 'I') or (j == 'o' or j == 'O') or (j == 'u' or j == 'U')):
                countPartTwo += 1
        return countPartOne == countPartTwo


result = Solution().halvesAreAlike("book")
print(result)

