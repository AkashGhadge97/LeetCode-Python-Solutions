# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

class Solution(object):
    def checkIfPangram(self, sentence):
        index = 97
        while index <= 122:
            if (sentence.count(chr(index)) == 0):
                return False
            index += 1
        return True


result = Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
print(result)
