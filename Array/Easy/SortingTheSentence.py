# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

class Solution(object):
    def sortSentence(self, s):
        lst = s.split(' ')
        i = 0
        while (i < len(lst)-1):
            if (int(lst[i][-1]) > int(lst[i+1][-1])):
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
                i = -1
            i += 1

        return ' '.join([i[0:len(i)-1] for i in lst])


result = Solution().sortSentence("is2 sentence4 This1 a3")
print(result)
