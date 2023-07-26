# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ''
        index = 0
        i = 0
        j = 0
        while (index < (len(word1+word2))):
            result = result + (word1[i] if (i < len(word1))
                               else '') + (word2[j] if (j < len(word2))else '')
            i += 1
            j += 1
            index += 1
        return result


result = Solution().mergeAlternately("ab", "pqrs")
print(result)
