# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
# Return the maximum number of words that appear in a single sentence.

import math

class Solution(object):
    def mostWordsFound(self, sentences):
        return max([len(i.split()) for i in sentences])


result = Solution().mostWordsFound(
    ["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
print(result)
