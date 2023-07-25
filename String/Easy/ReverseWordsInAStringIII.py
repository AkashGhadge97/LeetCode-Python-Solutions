#Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution(object):
    def reverseWords(self, s):
        splittedStr = s.split(" ")
        final = []
        for i in splittedStr:
            final.append(i[::-1])
        return " ".join(final)


result = Solution().reverseWords("Let's take LeetCode contest")
print(result)
