# You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
# Return the decoded message.

class Solution(object):
    def decodeMessage(self, key, message):
        lst = []
        for i in key:
            if i not in lst:
                lst.append(i)

        refDict = {}
        j = 97
        for i in lst:
            if i == ' ':
                continue
            refDict[i] = chr(j)
            j += 1

        refDict[' '] = ' '

        decodedMsg = ""
        for i in message:
            decodedMsg += refDict[i]

        return decodedMsg

result = Solution().decodeMessage(
    "eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb")
