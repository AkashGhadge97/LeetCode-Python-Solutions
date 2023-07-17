# You are given a 0-indexed array words consisting of distinct strings.

# The string words[i] can be paired with the string words[j] if:

# The string words[i] is equal to the reversed string of words[j].
# 0 <= i < j < words.length.
# Return the maximum number of pairs that can be formed from the array words.

# Note that each string can belong in at most one pair.

class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        words = set(words)
        count = 0
        result = []
        for i in words:
            if (i[::-1] in words and i != i[::-1] and [i[::-1], i] not in result):
                result.append([i, i[::-1]])
        return len(result)


result = Solution().maximumNumberOfStringPairs(["cd", "gd", "pg", "iq", "eh", "ce", "kd", "fp", "mk", "ob", "xn", "nx", "pf", "so", "ax", "qi", "dn", "lx", "ct", "yv", "km",
                                                "ec", "he", "dk", "mc", "zh", "hz", "dc", "cm", "ud", "ms", "os", "zx", "xa", "vy", "gp", "xz", "if", "bo", "oa", "xl", "pk", "dg", "tc", "nd", "kp", "du", "sm", "ao", "fi"])
print(result)
