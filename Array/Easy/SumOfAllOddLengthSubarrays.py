# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
# A subarray is a contiguous subsequence of the array.

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        total = 0
        for i in range(0, len(arr)):
            for j in range(1, len(arr)+1):
                print(arr[i:j])
                if (len(arr[i:j]) % 2 == 1):
                    total += sum(arr[i:j])
        return total


result = Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3])
print(result)
