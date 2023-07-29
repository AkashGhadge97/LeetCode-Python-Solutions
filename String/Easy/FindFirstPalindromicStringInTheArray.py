# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

class Solution(object):
    def firstPalindrome(self, words):
        for i in words:
            if ( i == i[::-1]):
                return i
        return ""

