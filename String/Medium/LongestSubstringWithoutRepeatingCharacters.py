# Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substring = ''
        length = 0
        for i in s:
            while i in substring:
                substring = substring[1:]

            substring += i
            length = max(length, len(substring))
        return length


result = Solution().lengthOfLongestSubstring("pwwkew")
print(result)
