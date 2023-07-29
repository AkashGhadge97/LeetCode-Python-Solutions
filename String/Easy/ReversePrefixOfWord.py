# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

class Solution(object):
    def reversePrefix(self, word, ch):
        if (ch in word):
            lst = []
            i = 0
            while (i < len(word)):
                lst.append(word[i])
                if (word[i] == ch):
                    break
                i += 1
            i += 1
            pending = ""
            while (i < len(word)):
                pending += word[i]
                i += 1
            lst = lst[::-1]
            return ''.join(lst)+pending
        return word


result = Solution().reversePrefix("abcdefd", "d")
print(result)
