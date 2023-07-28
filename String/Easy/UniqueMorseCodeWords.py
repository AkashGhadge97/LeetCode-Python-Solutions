# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

from unittest import result


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morderDict = {}
        j = 97
        for i in morse:
            morderDict[chr(j)] = i
            j += 1

        newSet = set()
        for i in words:
            morseCode = ''
            for j in i:
                morseCode += morderDict[j]
            newSet.add(morseCode)

        return len(newSet)


result = Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
print(result)
