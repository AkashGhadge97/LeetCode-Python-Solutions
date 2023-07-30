# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        result = ""
        for i in ransomNote:
            if i not in magazine:
                return False
            magazine = magazine.replace(i, '', 1)
        return True


result = Solution().canConstruct("aa", "ab")
print(result)
